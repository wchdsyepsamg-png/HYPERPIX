$ErrorActionPreference = "Stop"

Write-Host "Bootstrapping HYPERPIX..."

if (-not (Get-Command node -ErrorAction SilentlyContinue)) {
  throw "Node.js 22+ is required."
}

if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
  throw "Python 3.11+ is required."
}

npm install

Push-Location "services/api"
python -m venv .venv
& ".\.venv\Scripts\python.exe" -m pip install --upgrade pip
& ".\.venv\Scripts\python.exe" -m pip install -e ".[dev]"
Pop-Location

Write-Host ""
Write-Host "HYPERPIX bootstrap complete."
Write-Host "Run .\scripts\dev-api.ps1 and .\scripts\dev-desktop.ps1 in separate terminals."
