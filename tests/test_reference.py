import json
import math
import sys
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from audit_reference import audit
from check_case_inputs import missing_items, REQUIRED

class ReferenceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.inputs=json.loads((ROOT/'data/reference/patel_2025_conditions.json').read_text())
        cls.output=audit(cls.inputs)
    def test_logic_nozzles(self):
        self.assertEqual(self.output['logic_nozzle_count'],144)
        self.assertEqual(self.output['HBM_nozzle_count'],60)
    def test_reference_area(self):
        self.assertTrue(math.isclose(self.output['logic_total_orifice_area_m2'],2.827433388230814e-5,rel_tol=1e-12))
    def test_velocity(self):
        self.assertAlmostEqual(self.output['logic_mean_jet_velocity_m_per_s'],2.3578510087688206,places=7)
    def test_hydraulic_power(self):
        self.assertAlmostEqual(self.output['reference_cooler_only_hydraulic_power_W'],3.2213333333333334,places=10)
    def test_heated_areas(self):
        self.assertEqual(self.inputs['logic_heated_area_mm2']+4*self.inputs['hbm_heated_area_each_mm2'],self.inputs['total_heated_area_mm2'])
    def test_missing_inputs_fail_closed(self):
        self.assertEqual(set(missing_items(ROOT/'configs/h100_case_manifest.json')),set(REQUIRED))

if __name__=='__main__':unittest.main()
