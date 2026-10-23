# Staged roadmap and objective go/no-go checks

This is a **dependency-based plan**, not a guarantee of performance or schedule.

| Gate | Deliverable | Do not proceed until |
|---|---|---|
| 0 Evidence | source register, geometry traceability, baseline thermodynamics, unresolved-input list | no numerical input is undocumented |
| 1 Reproduction | experimental 2.5D heater + jet cooler reproduction | full wetted geometry, materials, heater mapping, coolant properties, input/output measurement definitions obtained; simulations pass conservation/mesh/validation checks |
| 2 H100-inspired test vehicle | traceable 700 W heater design, thermal interface, documented geometry | reliable mechanical and thermal specifications, or explicitly a non-H100-compatible research heater |
| 3 Comparison | verified CFD baseline and modified-geometry cases | same power, fluid, inlet T, measured flow or pump curve, interface treatment and convergence standards across alternatives |
| 4 Fabrication | sealed pressure-tested manifolds, heater fixture, instrumentation and test procedure | manufacturability, safety, leak test and calibrated sensors documented |
| 5 Validation | experimental thermal and hydraulic performance | temperature / heat balance / pressure results with uncertainty and repeatability; comparator measured under identical conditions |

## Work packages

1. **Reproduce published paper (Patel et al., 2025).** Start with the demonstrated nozzle and heated areas. Request remaining dimensions from the authors if the publication lacks details. Define actual measured locations, not assumed die junctions.
2. **Select one OpenFOAM distribution/version.** This repo targets **OpenFOAM Foundation v14**; do not copy syntax blindly from OpenCFD releases. Build official tutorials first.
3. **Numerical verification.** Grid-convergence study, sensitivity to numerical schemes / relaxation / physical time step when relevant, mass conservation, and fluid/solid energy closure.
4. **Experimental validation.** Compare measured average surface temperatures and full-cooler pressure drop at matched published conditions; report absolute and relative errors, include paper uncertainty.
5. **H100-class design.** Keep *700 W package total* distinct from a fictitious 700 W central-die source. Obtain actual mounting drawings and heat allocation or use a clearly identified custom heater layout.
6. **Design changes.** Change jet pitch, diameter, target clearance, flow distribution/manifold only after benchmark validation. Report `T_max`, thermal resistance with stated definition, pressure drop, pumping power, and Pareto tradeoff.
7. **Manufacturing/testing.** Leak-tightness, plumbing, pump curve, temperature sensors, thermal insulation, uncertainty and repeatability.

## Optimization objective

No arbitrary universal numeric targets are claimed. First compare at **the same measured heat load, coolant inlet temperature, fluid properties and volumetric flow**. Then compare at **equal measured pumping power**; equal-flow and equal-power comparisons answer different questions.

CFD predicts, it does not prove physical H100 operating margin. Testing an energized H100 must not be attempted until the package, interfaces, sensors, leak protection, and temperature constraints are independently verified.
