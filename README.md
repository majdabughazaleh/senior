# H100-class 700 W jet-impingement cooling — engineering research

**Status (23 Oct 2026): source-supported reference database and scripts verified. No OpenFOAM solver run, validated 3D jet-cooling case, H100-compatible CAD, or experimental H100 results yet.**

Goal: reproduce published multi-chip jet-impingement experiments and test whether a modified geometry improves the combined thermal/hydraulic performance at a **700 W class package load**. This is **not** a claim of H100 package compatibility or a completed cooling system.

## Evidence policy

- Every numerical input must have an identified origin: textbook equation, peer-reviewed experiment, manufacturer datasheet, or an *explicit and justified experimental design choice* (never silently inferred).
- Separate measured inputs, derived outputs, and design variables. A chosen boundary condition is **not** a manufacturer's specification.
- Unknown chip-to-HBM heat splits, H100 thermal limits, coolant properties, contact resistances, interface dimensions, material properties and pump efficiencies remain unresolved until sourced or measured.
- No fabricated CFD contours or performance predictions. **The project repository contains no runnable jet-impingement CFD model (the official OpenFOAM tutorial can now be run as a software smoke test).**
- Do not upload proprietary package drawings, manufacturer-confidential data, or the copyrighted journal PDF. Link to its DOI instead.

## Quick start (works without OpenFOAM)

```bash
python3 -m unittest discover -s tests -v
python3 scripts/audit_reference.py
python3 scripts/check_case_inputs.py configs/h100_case_manifest.json
```

The last command intentionally **fails** until the missing H100-specific inputs are supplied with citations. This is a safety gate, not a software error.

## CFD setup

Open in **GitHub Codespaces** using `.devcontainer` (experimental OpenFOAM Foundation **14** setup; construction of this image has **not** been verified here). After starting, check:

```bash
source /opt/openfoam14/etc/bashrc
foamVersion
which foamRun
```

OpenFOAM is not hosted or executed *by the GitHub repository itself*. Codespaces is cloud Linux compute and Actions tests the lightweight Python calculations. Full-scale mesh convergence and CHT simulations should use a suitably resourced workstation or university HPC cluster.

The `cfd/` folder deliberately holds a design checklist and no unverified nozzle-to-target distances, mesh, or boundary conditions. The new `scripts/run_official_openfoam_smoke_test.sh` runs an **unaltered** official v14 tutorial (software verification only); after that, use the v14 `foamMultiRun` fluid/solid tutorial as a verified syntax starting point for a source-supported physical model.

## Project deliverables

- [Design roadmap](docs/ROADMAP.md)
- [CFD verification and validation protocol](docs/CFD_VALIDATION_PLAN.md)
- [Missing input register](docs/DATA_GAPS.md)
- [Evidence sources](docs/SOURCES.md)
- [Reference experimental inputs](data/reference/patel_2025_conditions.json)
- [Measured logic surface temperature data](data/reference/patel_2025_logic_surface_temperatures.csv)
- [Design decisions log](docs/DECISIONS.md)

## Publication and privacy

Recommend a **private GitHub repository initially** until project ownership, potential IP disclosure, and partner permissions are clear. A public repository could disclose ideas before patent review. Keep mesh/results outputs in separate storage when large; Git is for traceable source artifacts. No license has been selected yet.

## Publishing and setup

- [GitHub upload and privacy](docs/GITHUB_SETUP.md)
- [OpenFOAM 14 tutorial smoke test](docs/OPENFOAM_SETUP.md)

## Phase 3 additions (verification harness, not cooling validation)

```bash
python3 scripts/thermal_reference.py --heat-to-water-w 700 --flow-lmin 4
python3 scripts/generate_reference_nozzle_patterns.py
# Only on a machine with official OpenFOAM Foundation 14 installed:
bash scripts/run_official_openfoam_smoke_test.sh
```

* [Detailed execution protocol](docs/PHASE3_EXECUTION.md)
* [140 experimental temperature readings](data/reference/patel_2025_all_surface_temperatures.csv) (Patel et al. Appendix C, Tables C.1–C.5)
* [Pressure-drop end points](data/reference/patel_2025_pressure_endpoints.csv), not an invented flow curve
* [IAPWS-based 20 C water reference values](data/reference/water_20C_IAPWS_based.json), tagged with source and constant-property limitation
* [2D drill grids](cad/reference_patterns/) drawn from the published nozzle count, diameter and pitch only
* [Actual CFD comparison script](scripts/validate_cfd_against_experiment.py) — needs an independently obtained CFD results CSV

**Caution:** the energy-balance ΔT calculates the conditional water-temperature rise for an explicitly specified heat transfer to water. It does not predict the H100 die, HBM or hot-spot temperature.
