# HELIOSTAT architecture

```
site gateway ──CSV──▶ ingest.CsvLoader ─┐
inverter fleet ─Modbus─▶ ingest.ModbusPoller ─┴─▶ quality.GapFiller ─▶ quality.OutlierFilter
                                                     │
                                                     ▼
                                          forecast.clear_sky_irradiance
                                          forecast.skill_score
                                                     │
                                                     ▼
                                            export.ParquetWriter
```

## Module boundaries

- `ingest` — talks to the field devices and normalises raw payloads.
- `quality` — repairs short measurement gaps and removes spikes.
- `forecast` — clear-sky reference model and skill scoring against persistence.
- `export` — writes the curated dataset to the planning team's data lake.

## Testing

The suite is grouped per module under `tests/`. Tests that cannot run reliably
on the shared CI fleet are marked `skip` or `xfail` with a reason that points at
the tracking ticket.
