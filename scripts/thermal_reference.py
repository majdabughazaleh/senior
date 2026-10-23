#!/usr/bin/env python3
"""Traceable reference-only water-side calculation, not H100 junction temperature.

Energy relation from steady-flow control-volume first law (Cengel & Boles).
The constant cp model is a documented reference approximation. It is NOT an
exact enthalpy integration or a prediction of a live GPU cooler.
"""
import argparse
import json
import math
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]

def reference_energy_balance(power_w, flow_Lmin, props):
    if power_w <= 0 or flow_Lmin <= 0:
        raise ValueError('Positive power and coolant flow required')
    volumetric_flow_m3_s=flow_Lmin * 0.001 / 60
    mass_flow_kg_s=props['density_kg_m3']*volumetric_flow_m3_s
    water_delta_T_K=power_w/(mass_flow_kg_s*props['cp_J_kg_K'])
    return {'heat_to_fluid_W':power_w,
            'flow_Lmin':flow_Lmin,
            'mass_flow_kg_s':mass_flow_kg_s,
            'constant_cp_deltaT_K':water_delta_T_K,
            'constant_cp_outlet_T_C':props['temperature_C']+water_delta_T_K}

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--heat-to-water-w',type=float,required=True,help='Conditional heat delivered to water, not assumed die power')
    p.add_argument('--flow-lmin',type=float,required=True)
    a=p.parse_args()
    props=json.loads((ROOT/'data/reference/water_20C_IAPWS_based.json').read_text())
    print(json.dumps({'classification':'reference constant-property water energy balance, NOT H100 prediction',
        'property_source':props['url'],**reference_energy_balance(a.heat_to_water_w,a.flow_lmin,props)},indent=2))
