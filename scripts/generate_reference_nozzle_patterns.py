#!/usr/bin/env python3
"""2D drill-pattern references, not full cooler CAD or a claimed full reconstruction.

Coordinate origin: chosen at centre of each regular array. Centering is a
coordinate convention, NOT evidence of registration within a physical H100.
Diameter/pitch/count published in Patel et al., Sec 2.1.1, page 5.
"""
import csv
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def centers(nx,ny,pitch_mm):
    for ix in range(nx):
        for iy in range(ny):
            yield ((ix-(nx-1)/2)*pitch_mm,(iy-(ny-1)/2)*pitch_mm)

def generate(output_dir):
    try:
        import ezdxf
    except ImportError as e:
        raise RuntimeError("DXF generation needs ezdxf: python3 -m pip install -r requirements-cad.txt (optional; pre-generated DXFs are included)") from e
    ref=json.loads((ROOT/'data/reference/patel_2025_conditions.json').read_text())
    output_dir=Path(output_dir);output_dir.mkdir(parents=True,exist_ok=True)
    pitch=ref['nominal_pitch_mm'];radius=ref['nominal_inlet_diameter_mm']/2
    for name,nx,ny in [('logic_12x12',12,12),('hbm_one_3x5',3,5)]:
        doc=ezdxf.new('R2010');msp=doc.modelspace()
        coords=list(centers(nx,ny,pitch))
        for xy in coords:msp.add_circle(xy,radius)
        doc.saveas(output_dir/(name+'.dxf'))
        with (output_dir/(name+'_centers.csv')).open('w',newline='') as f:
            w=csv.writer(f);w.writerow(['x_mm','y_mm','nominal_diameter_mm'])
            for x,y in coords:w.writerow([x,y,2*radius])
    (output_dir/'README.txt').write_text("""PATTERN DATA ONLY: relative coordinates constructed from published
nozzle diameter, count and pitch (Patel et al. 2025, p. 5).
No plate thickness, jet standoff, HBM registration, manifold cavity,
port positions, seal or mounting geometry is implied or supplied.
NOT a build-ready GPU cooler or validated experiment reproduction.
""")
    return output_dir
if __name__=='__main__':
    import sys
    loc=Path(sys.argv[1]) if len(sys.argv)>1 else ROOT/'cad/reference_patterns'
    generate(loc)
    print('Generated 144 and 15-hole 2D patterns in',loc)
