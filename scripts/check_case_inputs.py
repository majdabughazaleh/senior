#!/usr/bin/env python3
"""Fail closed when H100 CFD inputs lack numeric values or provenance."""
import json
import sys
from pathlib import Path

REQUIRED=[
 'h100_mounting_interface','h100_heat_flux_map','h100_die_temperature_limit',
 'h100_hbm_temperature_limit','thermal_contact_resistances',
 'coolant_name_and_composition','coolant_inlet_temperature_K',
 'coolant_flow_or_pump_curve','temperature_dependent_material_properties']

def missing_items(path):
    data=json.loads(Path(path).read_text())
    missing=[]
    for key in REQUIRED:
        obj=data.get(key,{})
        if not isinstance(obj,dict) or obj.get('value') in (None,'') or not obj.get('source'):
            missing.append(key)
    return missing

if __name__=='__main__':
    path=Path(sys.argv[1]) if len(sys.argv)>1 else Path('configs/h100_case_manifest.json')
    missing=missing_items(path)
    if missing:
        print('BLOCKED: cannot declare an H100-specific CFD model ready. Missing verified inputs:')
        for key in missing: print(' -',key)
        sys.exit(2)
    print('Manifest completeness check passed. This is NOT a physical validation.')
