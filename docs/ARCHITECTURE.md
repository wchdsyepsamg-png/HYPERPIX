# HYPERPIX Architecture

## Principle

The UI should never depend directly on a particular AI model. Every model is accessed through a stable service/adaptor boundary.

```text
Desktop UI
   |
   v
FastAPI
   |
   +--> Analyzer
   +--> Enhancement Pipeline
           |
           +--> Super Resolution Adapter
           +--> Face Restore Adapter
           +--> Denoise Adapter
           +--> Deblur Adapter
           +--> Depth Adapter
```

## Why

- Models can be swapped independently.
- CPU and GPU implementations can coexist.
- Cloud processing can be added later.
- Model licenses can be tracked separately.
- Testing does not require every heavyweight model to be installed.

## Processing contract

Future enhancement requests should contain:

- requested operations
- operation strengths
- authentic/generative mode
- desired output dimensions
- desired output format
- hardware preference

The API returns:

- processed image reference
- operations actually applied
- processing duration
- warnings
- model versions
