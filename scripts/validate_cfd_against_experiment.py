#!/usr/bin/env python3
"""Compare ALREADY-OBTAINED simulation surface means to paper Appendix C.

Input CSV has: cooler_flow_Lmin,logic_heater_power_W,region,simulated_avg_surface_T_C.
NO numerical simulations or performance predictions are generated here.
Exact experimental points must match; no interpolation or invented data.
"""
import argparse
import csv
from pathlib import Path
from math import sqrt

ROOT=Path(__file__).resolve().parents[1]
FIELD=('cooler_flow_Lmin','logic_heater_power_W','region')

def key(row):
    return (round(float(row['cooler_flow_Lmin']),6),int(row['logic_heater_power_W']),row['region'].strip().upper())

def compare(simulated, experimental):
    ref={key(r):float(r['reported_avg_surface_T_C']) for r in experimental}
    errors=[]; used=set(); extra=[]
    for r in simulated:
        k=key(r)
        if k in used: raise ValueError(f'Duplicate simulation comparison point: {k}')
        used.add(k)
        if k not in ref:
            extra.append(k);continue
        val=float(r['simulated_avg_surface_T_C'])
        delta=val-ref[k]
        errors.append({'flow_Lmin':k[0],'logic_power_W':k[1],'region':k[2],
                       'experiment_C':ref[k],'simulated_C':val,'error_C':delta,
                       'abs_error_C':abs(delta)})
    if not errors: raise ValueError('No matched experimental conditions found')
    return {'matched':len(errors),'unmatched_simulations':extra,
            'mae_C':sum(x['abs_error_C'] for x in errors)/len(errors),
            'rmse_C':sqrt(sum(x['error_C']**2 for x in errors)/len(errors)),
            'max_abs_error_C':max(x['abs_error_C'] for x in errors),
            'unmatched_experiment_count':len(ref)-len(errors),
            'details':errors}

if __name__=='__main__':
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('simulation_csv',type=Path)
    ap.add_argument('--detail-csv',type=Path)
    a=ap.parse_args()
    if not a.simulation_csv.is_file(): ap.error('Simulation file does not exist: no CFD results are available to validate')
    with a.simulation_csv.open(newline='') as f:sim=list(csv.DictReader(f))
    with (ROOT/'data/reference/patel_2025_all_surface_temperatures.csv').open(newline='') as f:exp=list(csv.DictReader(f))
    try: out=compare(sim,exp)
    except (ValueError,KeyError) as e:ap.error(str(e))
    for k in ('matched','mae_C','rmse_C','max_abs_error_C','unmatched_experiment_count'):
        print(f'{k}: {out[k]}')
    if out['unmatched_simulations']: print('UNMATCHED simulation cases (not silently interpolated):',out['unmatched_simulations'])
    print('These are comparison statistics, NOT proof of validation. Confirm matching boundary conditions, observation definitions, grid independence, and uncertainties.')
    if a.detail_csv:
        with a.detail_csv.open('w',newline='') as f:
            w=csv.DictWriter(f,fieldnames=list(out['details'][0]));w.writeheader();w.writerows(out['details'])
