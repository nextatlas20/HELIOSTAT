# Test Quarantine Ledger

Release engineering keeps this ledger so that no disabled test is forgotten.
Every test that carries an unconditional `skip` or `xfail` marker on the active
branch appears in the table below, and the summary counts are regenerated
whenever the ledger is refreshed.

## Quarantined tests

| Module | Test | Status | Reason | Since |
| --- | --- | --- | --- | --- |
| tests/export/test_parquet_writer.py | test_roundtrip_empty_frame | skip | pyarrow 17 segfault on empty schema, EXP-19 | release/2.0 |
| tests/forecast/test_clear_sky.py | test_airmass_rounding | skip | awaiting rounded constants, FORE-81 | release/2.0 |
| tests/forecast/test_clear_sky.py | test_linke_turbidity_dst | xfail | numeric tolerance too tight, FORE-77 | release/2.0 |
| tests/forecast/test_skill_score.py | test_pinball_loss_by_quantile | skip | needs reference values from v2 model | release/2.0 |
| tests/ingest/test_modbus_poller.py | test_batch_window_alignment | skip | blocked by ING-455 register map change | release/2.0 |
| tests/ingest/test_modbus_poller.py | test_reconnect_after_timeout | xfail | hardware simulator drops frames; ING-387 | main |
| tests/quality/test_gap_filler.py | test_linear_fill_across_dst | skip | pending DST fixture (QUAL-118) | main |
| tests/quality/test_gap_filler.py | test_short_gap_threshold | xfail | threshold under review, QUAL-233 | release/2.0 |

## Summary

- Quarantined tests: 8
- skip: 5
- xfail: 3
- New on release/2.0: 6
- Cleared since main: 3
