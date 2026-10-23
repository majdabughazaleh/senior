# Source register (checked 2026-10-23)

| ID | Source | Used for | Link / location |
|---|---|---|---|
| P25 | A. Patel, K. Yogi, G. Sahu, T. Wei (2025), “Multi-chip Jet impingement cooling for heat dissipation in 2.5D integrated system with 1 kW+ thermal design power”, *International Journal of Heat and Mass Transfer* **244**, 126978 | jet geometry, experimental boundary conditions, Tables C.1–C.5, measured Δp | https://doi.org/10.1016/j.ijheatmasstransfer.2025.126978 ; Section 2.1.1 p.5; Appendix C pp.22–23 |
| NV-H100 | NVIDIA H100 product specification | H100 SXM up to 700 W configurable TDP | https://www.nvidia.com/en-us/data-center/h100/ |
| OF-14 | OpenFOAM Foundation 14 Ubuntu installation guide | supported package, install commands and v14 tutorial workflow | https://openfoam.org/download/14-ubuntu/ |
| GH-CODES | GitHub Codespaces documentation | browser-hosted Linux containers and compute types | https://docs.github.com/en/codespaces/about-codespaces/what-are-codespaces |
| GH-ACTIONS | GitHub Actions usage limits | CI limits vs resource-intensive simulations | https://docs.github.com/en/actions/reference/limits |
| C-T | Y. A. Çengel and M. A. Boles, *Thermodynamics: An Engineering Approach* | steady-flow energy conservation | Textbook; edition-specific chapter/page to be logged before verbatim equation citation |
| C-HT | Y. A. Çengel and A. J. Ghajar, *Heat and Mass Transfer: Fundamentals & Applications* | conduction, convection, thermal resistance, forced convection | Textbook; edition-specific chapter/page to be logged before verbatim equation citation |

Do not copy the whole copyrighted paper into public GitHub. Use DOI and reproduce only original facts/derived calculations. Specific textbook page references are not given until the edition is established.


## Phase 3 sources (23 Oct 2026)

- **P25 Appendix C** (Patel et al., *International Journal of Heat and Mass Transfer*, 244, 126978, 2025; DOI 10.1016/j.ijheatmasstransfer.2025.126978): Tables C.1–C.5, printed pp. 22–23, all 140 temperature records. Source is **copper heater surface**, not H100 junction.
- **P25 conclusion** (p. 17): measured cooler pressure drop endpoint 4.15 kPa (1 L/min) and 48.32 kPa (4 L/min); cannot interpolate unknown midpoints.
- **W20** IAPWS-IF97/IAPWS R12-08 as implemented and published by The Engineering Handbook, 20 C and 1.013 bar: https://enghandbook.com/thermodynamic-calculators/water/ (third-party implementation, not independently endorsed by IAPWS; only reference energy balance).
- **OF14 official**: https://openfoam.org/download/14-ubuntu/ and https://doc.cfd.direct/openfoam/user-guide-v14/introduction and https://cpp.openfoam.org/v14/foamMultiRun_8C.html.

- **P25T** Patel, Akshat Hetal (2025), Purdue University MS thesis, *Direct on-chip cooling of heterogeneously integrated packages using single and two-phase jet impingement*, https://hammer.purdue.edu/articles/thesis/_b_DIRECT_ON-CHIP_COOLING_OF_HETEROGENEOUSLY_INTEGRATED_PACKAGES_USING_SINGLE_AND_TWO-PHASE_JET_IMPINGEMENT_b_/28848197 . This is a university-hosted primary source; full thesis figures/details still require inspection before inserting any geometry values.
