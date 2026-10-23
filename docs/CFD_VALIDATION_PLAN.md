# OpenFOAM CFD protocol (planned; no simulation yet)

**Software:** OpenFOAM Foundation v14 (not OpenCFD v2606). Record `foamVersion`, package patch level, operating system, mesh generator, numerical schemes, turbulence model, revision hash, compiler and CPU configuration for each released run.

## A. Reconstruct the experiment, not an imagined GPU

The publication has 144 central logic inlet nozzles (12×12), 60 peripheral inlet nozzles (4×3×5), 0.5 mm inlet diameter, 2 mm pitch, 676 mm² heated logic face and total heated area 1060 mm². For the series arrangement the full flow passes through the central nozzle array. Source: Patel et al., Section 2.1.1 and Fig. 3, p. 5; Appendix C pp. 22–23.

**Not yet published/checked sufficiently for an executable case:** full internal wetted manifold geometry, nozzle-to-heater gap for each region, inlet/outlet cross-sections, complete 3D heater dimensions and actual seal/insulation geometry, thermal contact models. No CFD case is generated until these are resolved or openly parameterized as experimental design choices.

## B. Boundary conditions

The published test used DI water at 20 °C, 1–4 L/min at listed flow rates, logic loads 500–1700 W, 4×40 W HBM blocks at the tabulated test conditions. The paper's 'fixed 40 W HBM' is **not** an H100 heat distribution.

Reference data must retain source/section/page. For any calculated property, record the reference standard and temperature interval; do not simply insert room-temperature viscosity/conductivity.

## C. Physics

For the ultimate reference recreation use 3D conjugate heat transfer (fluid + copper solids and needed thermal contact/insulation), and match the experiment's methodology. Start with an official *OpenFOAM 14* tutorial; identify its current multi-region solver and verify case-format compatibility before copying boundary files. Resistances: distinguish junction-to-liquid, heater surface-to-inlet and chip area-normalized values.

## D. Verification and validation (V&V)

1. Geometric integrity: physical dimensions/volumes/nozzle counts equal source or documented design parameters.
2. `checkMesh` passes; near-wall resolution and transition/turbulence models justified for actual Reynolds and jet physics.
3. At least three successively refined grids; report mesh metrics and Richardson/GCI analysis where asymptotic behavior supports it. No default arbitrary percent grid criterion.
4. Mass closure: inflow minus outflow and leakage; energy closure: heated solids vs. fluid enthalpy rise plus boundary losses, with clearly defined measurement uncertainty.
5. Compare temperature at same actual experimental thermocouple/extrapolated surface positions and pressure between same tapping points. Do not compare mean surface to maximum junction.
6. Record residual and monitor histories, sensitivities to turbulence model/BC/thermal resistance, and any unvalidated extrapolations.
7. No fabricated quantitative improvement results. Present missing outcomes as 'not simulated' or 'not measured'.

## E. Controlled comparison

At identical inlet coolant, chip heating distribution, flow, and contact conditions: baseline vs redesigned jet/nozzle geometry; also repeat using equal pumping-power condition once actual pump efficiency and loop losses are characterized. A lower pressure drop **alone** does not imply superiority if thermal resistance increases.
