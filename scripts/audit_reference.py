#!/usr/bin/env python3
"""Reconstruct only source-supported reference geometric/hydraulic arithmetic.
No pump efficiency, measured die temperatures, or unverified water properties.
"""
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def audit(data):
    n_logic = data['central_logic_inlet_nozzles']
    n_hbm = data['hbm_modules']*data['hbm_nozzle_array_rows']*data['hbm_nozzle_array_columns']
    diameter_m = data['nominal_inlet_diameter_mm']*1e-3
    area_m2 = n_logic*math.pi*diameter_m**2/4
    flow_m3s = data['reference_flow_L_per_min']*1e-3/60
    pressure_pa = data['reference_cooler_delta_p_kPa']*1e3
    return {
        'logic_nozzle_count':n_logic,
        'HBM_nozzle_count':n_hbm,
        'logic_total_orifice_area_m2':area_m2,
        'logic_mean_jet_velocity_m_per_s':flow_m3s/area_m2,
        'reference_cooler_only_hydraulic_power_W':flow_m3s*pressure_pa,
        'reference_logic_heated_area_mm2':data['logic_heated_area_mm2'],
        'reference_total_heated_area_mm2':data['total_heated_area_mm2']
    }

if __name__=='__main__':
    data=json.loads((ROOT/'data/reference/patel_2025_conditions.json').read_text())
    print('Published reference only: '+data['citation_url'])
    for k,v in audit(data).items():print(f'{k}: {v:.8g}' if isinstance(v,float) else f'{k}: {v}')
    print('NOTE: 3D geometry, pump electric power, H100 interface and chip junction temperatures NOT calculated.')
