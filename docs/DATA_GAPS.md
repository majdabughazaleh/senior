# Gaps that block an honest H100-compatible design

| Parameter | Source required | Impact | Status |
|---|---|---|---|
| H100 SXM package outer dimensions, allowed contact footprint, standoff heights, keep-outs and mounting | NVIDIA or approved OEM mechanical drawing | CAD fit and seals | MISSING |
| Per-region GPU die/HBM heat-source split and heat-flux maps | official measurement, published thermography or calibrated test vehicle | input heat distribution | MISSING |
| Valid H100 die and HBM temperature limits under liquid cooling | OEM thermal design guide | safe operating threshold | MISSING |
| Lidded/lidless state, thermal path and contact resistance for selected package | OEM drawings and interface materials | silicon-to-coolant thermal model | MISSING |
| Representative working coolant, inlet T, pressure, chemistry for deployment | data-center plant/OEM operating requirements | thermohydraulic performance | MISSING |
| Full nozzle gaps, lateral manifold and outlet geometry in published study | paper supplementary data or correspondence with authors | full 3D CFD reproduction | MISSING |
| Full temperature-dependent fluid and solid properties | standard tables, IAPWS, material manufacturer | solver material dictionaries | MISSING |
| Pump Q–Δp curve, efficiency vs operating point | measured pump or manufacturer data | actual electric pumping power | MISSING |
| Conventional baseline at identical conditions | independent test or OEM validated curves | performance claim | MISSING |

**No-assumptions rule:** when unavailable, mark `MISSING`. Engineering design eventually requires choices (e.g. target conditions, mesh settings, dimensions); those are **explicit design decisions**, not verified facts, and must be justified and validated.

**Potential primary-source follow-up:** Purdue-hosted 2025 Akshat Patel MS thesis (link in SOURCES.md) may contain additional fabrication dimensions, but its content has not been verified for the missing dimensions. Request original CAD and nozzle standoff from corresponding author if unavailable.
