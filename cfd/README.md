# CFD model — gated

No executable 3D CFD case is included: essential geometry, fluid/solid properties and interface data are not yet verified. **Do not confuse this with having reproduced the experiment.**

Target environment: OpenFOAM Foundation 14; run official tutorials before building project dictionaries. The Foundation 14 solver structure may differ from tutorials online for the OpenCFD distribution; never mix without verifying.

## Readiness gate

1. `python3 scripts/check_case_inputs.py configs/h100_case_manifest.json` must pass for an H100-specific model.
2. Document every unresolved/reference datum and design choice, their source and uncertainty.
3. Obtain complete reference wetted CAD with all gap, nozzle, manifold and heater geometry. If reconstructing missing geometry, label it *a newly designed approximation*, not the authors' experimental cooler.
4. Mesh `checkMesh`; verify 3 grid levels, conservation, monitor stability, model sensitivities.
5. Validate temperatures and pressure against published readings at matched source conditions before making any improvement claim.

## Available software verification case
Run `bash scripts/run_official_openfoam_smoke_test.sh` from repository root with OpenFOAM 14 installed. It copies and solves the **unchanged official Foundation tutorial** to `cfd/runs/tutorial_pitzDailySteady/` (ignored by Git). This case is not a jet, does not solve heat transfer and must not be used as evidence for H100 cooling.
