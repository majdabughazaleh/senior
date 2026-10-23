# Laboratory thermal-test protocol — planning only

**No equipment has been selected or calibrated and no experiment has been run.**

## Reference condition to reproduce first

Purdue Patel et al. (2025), Appendix C: 500 W central heater plus four peripheral 40 W heaters = **660 W total**; DI water nominal **20°C** inlet and **4 L/min** in published experiments. This is **a paper-reproduction point**, not H100 power distribution. Published average copper-heater temperatures for this point (Tables C.1–C.5): central 45.48°C, HBM1 44.25°C, HBM2 38.60°C, HBM3 44.34°C, HBM4 39.25°C. The article does NOT provide a complete public CAD for an identical reproduction.

## Required measured channels

* Electrical heater powers: measured voltage and current **per heater**, or independent calibrated power meter. Convert to power by appropriate electrical measurement methods; do not substitute a nameplate rating.
* Water coolant inlet/outlet temperatures and measurement locations; measure mixing effectiveness and uncertainty.
* Flow rate and its calibration; identify coolant composition and physical properties at measured temperatures.
* Differential pressure taps directly across test cooler, not the entire loop alone.
* Heater surface temperature at defined positions. Reproduce reference extrapolation only if heater solid geometry, conductivity, thermocouple positions and heat-flux gradients are established.
* Ambient losses, heat losses through mounts/insulation, pump input electrical power and measurement uncertainty.

## Calculated quantities (Çengel and Boles, Thermodynamics; Çengel and Ghajar, Heat Transfer)

Steady energy accounting:

`Q_water = m_dot * (h_out - h_in)` (if properly characterized; enthalpy may require integrating cp over measured temperature interval).

`Q_heat_to_test = sum(V_i I_i)` when electrical quantities represent actual DC heater input and corrections are applied.

`Q_heat_to_test = Q_water + Q_losses + energy_storage_rate` with sign conventions documented. At steady state storage rate is zero.

`W_hyd_cooler = delta_p_cooler * volumetric_flow`, **not** equal to pump electrical power.

Thermal-resistance reporting MUST name hot location (`max`, `mean` or individual sensor), reference coolant temperature, whether package contact/interface is included, and whether the value is area-normalized.

## Acceptance decision

No arbitrary +/- percentage or fixed hot-spot limit may be inserted as a verified performance requirement. The team must establish those values from the measurement uncertainty budget, OEM requirements and sponsor/academic test criteria. Report actual measurements alongside numerical predictions and uncertainties, not selected favorable points.

Do not expose a live H100 to experimental direct-on-chip fluid impingement without package approval and independent leak/pressure qualification.
