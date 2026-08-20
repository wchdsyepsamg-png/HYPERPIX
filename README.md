# HYPERPIX

**HYPERPIX** is an AI-assisted image enhancement application focused on extracting the highest useful quality from an image while clearly separating restoration from AI-generated reconstruction.

## Architecture

```text
HYPERPIX/
├─ apps/
│  └─ desktop/              # React + Vite desktop UI
├─ services/
│  └─ api/                  # FastAPI image-analysis/enhancement API
├─ packages/
│  └─ shared/               # Shared schemas/types later
├─ models/                  # Local AI model weights (ignored by Git)
├─ assets/                  # Branding/sample assets
├─ scripts/                 # Setup/dev helpers
├─ docs/                    # Architecture, roadmap, model notes
└─ .github/                 # CI, templates, Dependabot
```

## MVP goals

- Import an image
- Analyze blur, brightness, dimensions, and quality signals
- Recommend enhancements
- Run a basic enhancement pipeline
- Compare before/after
- Export the processed image
- Add GPU-backed super-resolution and face restoration as model adapters

## Local development

### Prerequisites

- Node.js 22+
- Python 3.11+
- Git

### Bootstrap on Windows

```powershell
Set-ExecutionPolicy -Scope Process Bypass
.\scripts\bootstrap.ps1
```

### Run

Terminal 1:

```powershell
.\scripts\dev-api.ps1
```

Terminal 2:

```powershell
.\scripts\dev-desktop.ps1
```

The API defaults to `http://127.0.0.1:8000`.

## Branch strategy

- `main` — stable/releasable
- `develop` — integration branch
- `feature/<name>` — new work
- `fix/<name>` — bug fixes
- `release/<version>` — release preparation

## Commit style

Use Conventional Commits:

```text
feat: add image analyzer
fix: prevent invalid image upload
docs: document model pipeline
chore: update dependencies
```

## Planned AI adapters

HYPERPIX will keep models behind adapters so they can be swapped without rewriting the application:

- Super-resolution: Real-ESRGAN-class adapter
- Face restoration: GFPGAN/CodeFormer-class adapter
- Denoising/deblurring adapters
- Depth estimation adapter for HyperDepth / HyperBokeh

Model weights are **not committed to Git**.
