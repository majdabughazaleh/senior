.PHONY: test audit check-inputs

test:
	python3 -m unittest discover -s tests -v

audit:
	python3 scripts/audit_reference.py

check-inputs:
	python3 scripts/check_case_inputs.py configs/h100_case_manifest.json

reference-thermal:
	python3 scripts/thermal_reference.py --heat-to-water-w 700 --flow-lmin 4

reference-patterns:
	python3 scripts/generate_reference_nozzle_patterns.py

openfoam-smoke:
	bash scripts/run_official_openfoam_smoke_test.sh
