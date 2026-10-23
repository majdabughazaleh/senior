#!/usr/bin/env bash
set -euo pipefail
if [[ ! -f /opt/openfoam14/etc/bashrc ]];then echo 'BLOCKED: OpenFOAM 14 is not installed' >&2;exit 2;fi
set +u;source /opt/openfoam14/etc/bashrc;set -u
command -v foamMultiRun >/dev/null || { echo 'BLOCKED: missing foamMultiRun' >&2;exit 2; }
echo 'Available multi-region tutorial examples (names only; no model is run):'
find "$FOAM_TUTORIALS" -maxdepth 5 -name regionProperties -print | head -40 || true
printf '
Select official Foundation 14 fluid/solid tutorial; consult its README and Allrun before running.\n'
