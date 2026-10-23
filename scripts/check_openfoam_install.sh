#!/usr/bin/env bash
set -euo pipefail
if [ ! -f /opt/openfoam14/etc/bashrc ]; then
  echo 'ERROR: OpenFOAM Foundation 14 profile not found at /opt/openfoam14/etc/bashrc' >&2
  exit 1
fi
# shellcheck disable=SC1091
source /opt/openfoam14/etc/bashrc
foamVersion
command -v blockMesh
command -v foamRun
printf '%s\n' 'OpenFOAM executables found. No research case was run.'
