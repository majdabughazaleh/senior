# OpenFOAM Foundation 14 startup and smoke test

Use the official instructions at https://openfoam.org/download/14-ubuntu/ rather than mixing commands from the separate OpenCFD OpenFOAM v2606 series.

When the experimental GitHub Codespaces image has successfully built:

```bash
source /opt/openfoam14/etc/bashrc
foamVersion
which foamRun
```

The official Foundation v14 Ubuntu guide documents the following *software installation smoke test*. It tests a standard **incompressible-flow benchmark**, **not** a jet cooler and **not** an H100 thermal result:

```bash
mkdir -p "$FOAM_RUN"
cd "$FOAM_RUN"
cp -r "$FOAM_TUTORIALS/incompressibleFluid/pitzDailySteady" .
cd pitzDailySteady
blockMesh
foamRun
```

If that example differs in a patched distribution, select the equivalent tutorial from that installed version and record it in `docs/DECISIONS.md`. For the research cooler, only proceed after obtaining full wetted geometry, complete fluid properties, heater distribution and interfaces, and a solver/tutorial demonstrably compatible with v14 multi-region conjugate heat transfer.
