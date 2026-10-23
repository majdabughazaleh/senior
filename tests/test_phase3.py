import csv
import json
import sys
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from thermal_reference import reference_energy_balance
from validate_cfd_against_experiment import compare
from generate_reference_nozzle_patterns import centers
class Phase3Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with (ROOT/'data/reference/patel_2025_all_surface_temperatures.csv').open(newline='') as f:
            cls.rows=list(csv.DictReader(f))
        cls.props=json.loads((ROOT/'data/reference/water_20C_IAPWS_based.json').read_text())
    def test_experiment_complete_as_published(self):
        self.assertEqual(len(self.rows),140)
        self.assertEqual({r['region'] for r in self.rows},{'LOGIC','HBM1','HBM2','HBM3','HBM4'})
        self.assertEqual(len({(r['region'],r['cooler_flow_Lmin'],r['logic_heater_power_W']) for r in self.rows}),140)
    def test_key_measured_surf_values(self):
        lookup={(r['region'],float(r['cooler_flow_Lmin']),int(r['logic_heater_power_W'])):float(r['reported_avg_surface_T_C']) for r in self.rows}
        self.assertEqual(lookup[('LOGIC',4.0,1700)],88.62)
        self.assertEqual(lookup[('LOGIC',4.0,500)],45.48)
        self.assertEqual(lookup[('HBM3',4.0,1700)],65.26)
    def test_conditional_thermal_balance(self):
        out=reference_energy_balance(700.0,4.0,self.props)
        self.assertAlmostEqual(out['constant_cp_deltaT_K'],2.510,delta=0.02)
        self.assertAlmostEqual(out['mass_flow_kg_s'],0.06654706667,places=8)
    def test_nonpositive_inputs_rejected(self):
        with self.assertRaises(ValueError):reference_energy_balance(700,0,self.props)
    def test_exact_match_metric(self):
        exp=[{'cooler_flow_Lmin':'4','logic_heater_power_W':'500','region':'LOGIC','reported_avg_surface_T_C':'45.48'}]
        sim=[{'cooler_flow_Lmin':'4.0','logic_heater_power_W':'500','region':'LOGIC','simulated_avg_surface_T_C':'46.48'}]
        out=compare(sim,exp)
        self.assertAlmostEqual(out['mae_C'],1.0)
        self.assertEqual(out['matched'],1)
    def test_missing_case_is_not_interpolated(self):
        ex=[{'cooler_flow_Lmin':'4','logic_heater_power_W':'500','region':'LOGIC','reported_avg_surface_T_C':'45.48'}]
        with self.assertRaises(ValueError):compare([{'cooler_flow_Lmin':'4','logic_heater_power_W':'700','region':'LOGIC','simulated_avg_surface_T_C':'51.00'}],ex)
    def test_geometry_patterns(self):
        logic=list(centers(12,12,2.0));hbm=list(centers(3,5,2.0))
        self.assertEqual(len(logic),144);self.assertEqual(len(hbm),15)
        self.assertEqual(min(x for x,y in logic),-11.0)
        self.assertEqual(max(x for x,y in logic),11.0)
        self.assertEqual(min(y for x,y in hbm),-4.0)
    def test_pressure_only_published_points(self):
        with (ROOT/'data/reference/patel_2025_pressure_endpoints.csv').open(newline='') as f:p=list(csv.DictReader(f))
        self.assertEqual(len(p),2)
        self.assertEqual({float(x['flow_Lmin']) for x in p},{1.,4.})
        self.assertEqual({float(x['measured_cooler_delta_p_kPa']) for x in p},{4.15,48.32})
if __name__=='__main__':unittest.main()
