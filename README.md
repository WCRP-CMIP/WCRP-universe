# WCRP Universe Controlled Vocabulary

The **WCRP Universe** is the central, shared repository of controlled vocabulary (CV) terms used across WCRP climate modelling projects (CMIP7, CORDEX, etc.). It provides the foundational definitions that project-specific CVs reference and build upon.

Each term is stored as a self-contained JSON file with [JSON-LD](https://json-ld.org/) context, organized by **data descriptor** (e.g. `variable/`, `experiment/`, `institution/`).

## Repository Structure

```
WCRP-universe/
├── activity/              # MIP activities (AerChemMIP, C4MIP, ...)
├── experiment/            # Experiment definitions (~494 terms)
├── variable/              # Physical variables (~2281 terms)
├── institution/           # Research institutions (~214 terms)
├── organisation/          # Consortia and organisations
├── realm/                 # Model realms (atmos, ocean, ...)
├── frequency/             # Output frequencies (mon, day, ...)
├── source/                # Model source descriptions
├── region/                # Geographic regions
├── grid_type/             # Grid type definitions
├── ...                    # 70+ data descriptors in total
├── esgvoc_manifest.yaml   # Version and release metadata
├── _src/                  # Pydantic models and generation scripts
└── _tests/                # Validation tests
```

Each data descriptor directory contains:
- `000_context.jsonld` — JSON-LD context mapping fields to schema.org URIs
- One `.json` file per term, named by its identifier

## Browsing Terms

You can browse terms directly on GitHub by navigating into any data descriptor directory. Each JSON file is a self-contained term definition.

**Examples:**

A variable (`variable/tas.json`):
```json
{
    "@context": "000_context.jsonld",
    "id": "tas",
    "type": "variable",
    "drs_name": "tas",
    "long_name": "Daily Minimum Near-Surface Air Temperature",
    "standard_name": "air_temperature",
    "units": "K"
}
```

An experiment (`experiment/abrupt-4xco2.json`):
```json
{
    "@context": "000_context.jsonld",
    "id": "abrupt-4xco2",
    "type": "experiment",
    "drs_name": "abrupt-4xCO2",
    "description": "Abrupt quadrupling of atmospheric carbon dioxide levels.",
    "activity": "cmip",
    "required_model_components": ["aogcm"],
    "min_ensemble_size": 1,
    "tier": 1
}
```

An institution (`institution/ipsl.json`):
```json
{
    "@context": "000_context.jsonld",
    "id": "ipsl",
    "type": "institution",
    "drs_name": "IPSL",
    "labels": ["Institut Pierre-Simon Laplace"],
    "location": [{"city": "Paris", "country": "France"}],
    "ror": "02haar591",
    "urls": ["https://www.ipsl.fr/en/"]
}
```

## Querying Terms with esgvoc

[**esgvoc**](https://github.com/ESGF/esgf-vocab) is the companion Python library for querying, searching, and validating controlled vocabulary terms across the universe and project-specific CVs.

### Installation

```bash
pip install esgvoc
```

### CLI usage

```bash
# Search for a term across the universe
esgvoc find "air_temperature" :variable

# Get a specific term
esgvoc get :variable:tas

# List all activities
esgvoc get :activity
```

### Python API

```python
from esgvoc.api import find_terms_in_universe, get_term_in_universe

# Full-text search
results = find_terms_in_universe("air_temperature")

# Get a specific term by ID
term = get_term_in_universe("tas")
```

For full documentation, see the [esgvoc documentation](https://esgf.github.io/esgf-vocab/).

## Contributing New Terms

Project CV managers who want to add new terms to the universe should follow this process:

### 1. Fork the repository

Fork [WCRP-CMIP/WCRP-universe](https://github.com/WCRP-CMIP/WCRP-universe) to your GitHub account.

### 2. Add your term

Create a new JSON file in the appropriate data descriptor directory. The term **must** conform to the Pydantic model for that data descriptor (models are defined in `_src/wcrp_universe/models/`).

Every term requires at minimum:
```json
{
    "@context": "000_context.jsonld",
    "id": "your-term-id",
    "type": "<data_descriptor_name>",
    "drs_name": "YourDRSName"
}
```

Additional fields depend on the data descriptor type. Refer to existing terms in the same directory as examples.

**Naming conventions:**
- The file name must match the `id` field (e.g. `id: "my-term"` goes in `my-term.json`)
- The `id` should be lowercase, using hyphens as separators
- The `drs_name` is the Data Reference Syntax (DRS) name, which may use different casing

### 3. Submit a Pull Request to `esgvoc_dev`

Open your PR against the **`esgvoc_dev`** branch (not `main`). This allows:
- Automated validation against the Pydantic data models
- Review by CV managers before the term is merged
- Testing in a staging environment before promotion to `main`

Once approved and merged into `esgvoc_dev`, changes will be promoted to `main` after a validation cycle.

## Versioning

Version information is tracked in `esgvoc_manifest.yaml`:

```yaml
cv_version: "1.0.2"
universe_version: "1.0.2"
esgvoc:
  min_version: "4.0.0"
```

## License

This work is licensed under [Creative Commons Attribution 4.0 International (CC BY 4.0)](LICENSE-CC-BY).
