#!/usr/bin/env bash
set -euo pipefail

rdir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
vdir="${rdir}/.blueish"

cd "${rdir}"

if [[ ! -d "${vdir}" ]]; then
    echo "[!] Virtual environment missing"
    echo "[!] Run ./install.sh first"
    exit 1
fi

source "${vdir}/bin/activate"

export PYTHONUNBUFFERED=1

python3 Main.py