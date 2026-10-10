#!/usr/bin/env bash
set -euo pipefail

rdir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
vdir="${rdir}/.blueish"
cd "${rdir}"

echo "[*] Pokemon Blueish installer"
echo "[*] Repo: ${rdir}"

if ! command -v python3 >/dev/null 2>&1; then
    echo "[!] python3 not found"
    echo ""
    echo "Please install python3 or add to PATH"
    exit 1
fi

echo "[*] Creating virtual environment..."
rm -rf "${vdir}"
python3 -m venv "${vdir}"

source "${vdir}/bin/activate"

echo "[*] Upgrading pip..."
python3 -m pip install --upgrade pip wheel setuptools

REQ_FILE=""

if [[ -f "${rdir}/Requirements.txt" ]]; then
    REQ_FILE="Requirements.txt"
elif [[ -f "${rdir}/Requirments.txt" ]]; then
    REQ_FILE="Requirments.txt"
else
    echo "[!] Could not locate requirements file"
    exit 1
fi

echo "[*] Installing dependencies from ${REQ_FILE}..."
python3 -m pip install -r "${REQ_FILE}"

echo "[*] Normalizing Windows path separators..."
python3 <<'PY'
from pathlib import Path

for path in Path(".").rglob("*"):
    if any(part.startswith(".") for part in path.parts):
        continue
    if path.suffix.lower() not in {".py", ".tmx", ".tsx"}:
        continue

    try:
        text = path.read_text(errors="ignore")
    except Exception:
        continue

    fixed = text.replace("\\", "/")

    fixed = fixed.replace("Lady3_down.png", "Lady3_Down.png")
    fixed = fixed.replace("Lady3_left.png", "Lady3_Left.png")

    if fixed != text:
        path.write_text(fixed)
        print(f"patched {path}")
PY

echo "[*] Verifying syntax..."
python3 -m py_compile Main.py

chmod +x "${rdir}/Start.sh"

echo
echo "[+] Installation complete"
echo "[+] Start game with:"
echo "    ./Start.sh"
