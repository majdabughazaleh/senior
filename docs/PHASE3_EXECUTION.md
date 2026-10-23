# Phase 3 execution: exact workflow (2026-10-23)

## Current evidence and boundary

This repository has **no run of OpenFOAM and no validation of an H100 cooling design**. It now includes a fail-closed experimental comparison harness and a way to run the **unchanged, official** OpenFOAM Foundation v14 tutorial.

### 1. Checks today (no CFD needed)

```bash
python3 -m unittest discover -s tests -v
python3 scripts/audit_reference.py
python3 scripts/thermal_reference.py --heat-to-water-w 700 --flow-lmin 4
python3 scripts/check_case_inputs.py configs/h100_case_manifest.json
```

The last command MUST return exit 2 until all H100 inputs have documented sources. Its failure means the engineering evidence is incomplete.

### 2. Official CFD smoke test on an OpenFOAM-14 machine

```bash
bash scripts/run_official_openfoam_smoke_test.sh
```

This copies the **official** `incompressibleFluid/pitzDailySteady` into an ignored `cfd/runs/` directory, runs `blockMesh`, `checkMesh` and `foamRun`, and saves logs. It is a solver/environment verification exercise, NOT a test of a microjet cooler. No project boundary conditions or invented nozzle lengths are fed into this tutorial.

`bash scripts/inspect_openfoam_cht_examples.sh` lists installed multi-region examples. For heat-transfer work, use the Foundation 14 multi-region solver `foamMultiRun`; it couples `fluid` and `solid` regions, governed by the official case documents. Do not copy older `chtMultiRegionFoam` from the separate OpenCFD release indiscriminately.

Sources: [official OpenFOAM Foundation 14 tutorial and installation](https://openfoam.org/download/14-ubuntu/); [official Foundation v14 user guide](https://doc.cfd.direct/openfoam/user-guide-v14/introduction); [official foamMultiRun documentation](https://cpp.openfoam.org/v14/foamMultiRun_8C.html).

### 3. Experimental temperature database

The 140 published temperatures in `data/reference/patel_2025_all_surface_temperatures.csv` are transcribed from **Tables C.1–C.5, pp. 22–23** of Patel et al. 2025. Each of the five surfaces (LOGIC, HBM1–4) has 28 reported cases. Missing/dash entries are **not interpolated**.

Once valid independent CFD predictions exist, create a CSV containing columns:

`cooler_flow_Lmin,logic_heater_power_W,region,simulated_avg_surface_T_C`

For example, compare predictions at the exact reported heater load, flow and surface definitions (not maximum-to-average, junction-to-surface or 700 W against 660 W):

```bash
python3 scripts/validate_cfd_against_experiment.py results_from_actual_CFD.csv --detail-csv errors.csv
```

The comparison reports MAE, RMSE and maximum absolute error, without a fabricated acceptance threshold. It does not check energy/pressure conservation automatically; those require additional monitored CFD fields. Validate solver discretisation independently before using any error figures.

### 4. Source-supported geometry files

`cad/reference_patterns` provides mathematically generated 12x12 (144) and 3x5 (15) inlet-hole grids, exactly 0.5 mm nominal hole diameter and 2 mm pitch. Origin choice and centering are just drawing conventions, **not** verified three-dimensional registration. Do not claim these reproduce manifold depths, jet-target spacing, fluid connections, or real H100 mounting.

### 5. Data that must be obtained next

1. **To reproduce paper faithfully:** wetted CAD/nozzle-to-chip distances, manifold heights, internal outlet cross-sections, heater geometry/contact paths, water fluid property data at operating temperature. Seek author supplementary files or measurements; until then cannot generate complete jet case without design hypotheses.
2. **To build an H100-compatible cooler:** OEM mechanical and thermal interface constraints, package power distribution, allowable temperatures and contact interface resistance. Without these no direct-H100 mount claim.
3. **To establish improvement:** a matched baseline tested on the same heater/coolant/manifold boundaries, including pressure tap positions, pump energy and contact conditions.

### Explicit go/no-go gates

* **Gate A (software):** official tutorial solves and logs archived; not proof of physics validation.
* **Gate B (experiment reconstruction):** complete and provenance-tagged geometry/BC, mass/energy conservation, grid study and temperature/pressure comparison.
* **Gate C (H100 proxy):** same power distribution and temperature definition as an instrumented H100-class thermal test vehicle.
* **Gate D (innovation):** demonstrate thermal advantage at **equal measured pumping energy**, or lower pumping power at equivalent thermal performance, plus buildability and reliability.

**Project decision now:** proceed with documented 700 W-class thermal test-vehicle research and the publication replication plan, but do not claim H100-compatible CAD or CFD-validated performance until Gates B–D are passed.


### Laboratory verification handoff

A separate [measurement protocol](MEASUREMENT_PROTOCOL.md) defines the required measurements and energy-balance sign conventions. This must be approved before claiming performance.

### Optional CAD library

The DXFs and center-coordinate CSVs are already generated. To regenerate CAD patterns, install the *optional* Python dependency from `requirements-cad.txt` in a suitable virtual environment and run `python3 scripts/generate_reference_nozzle_patterns.py`. All reference arithmetic and unit tests work with the standard library alone.
