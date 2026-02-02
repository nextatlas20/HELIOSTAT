# HELIOSTAT

HELIOSTAT normalises rooftop photovoltaic inverter telemetry and produces
short-horizon irradiance forecasts for the grid planning team.

## Repository layout

| Path | Contents |
| --- | --- |
| `src/heliostat/` | ingestion, quality-control and forecasting modules |
| `tests/` | pytest suite, grouped by subsystem |
| `docs/` | architecture notes and the test quarantine ledger |

## Branch model

- `main` — the 1.9 maintenance line.
- `release/2.0` — the 2.0 hardening branch cut from `main`.

## Local development

```bash
pip install -e ".[dev]"
pytest tests/ -q
```

## Documentation

- `docs/ARCHITECTURE.md` — module boundaries and data flow.
- `docs/TEST_QUARANTINE.md` — ledger of tests that are currently disabled.
