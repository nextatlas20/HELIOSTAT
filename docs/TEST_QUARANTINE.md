# Test Quarantine Ledger

Release engineering keeps this ledger so that no disabled test is forgotten.
Every test that carries an unconditional `skip` or `xfail` marker on the active
branch appears in the table below, and the summary counts are regenerated
whenever the ledger is refreshed.

## Quarantined tests

| Module | Test | Status | Reason | Since |
| --- | --- | --- | --- | --- |
| tests/forecast/test_skill_score.py | test_pinball_loss_quantiles | skip | needs reference values from v2 model | main |
| tests/ingest/test_csv_loader.py | test_handles_cp1252_fallback | skip | fixture needs re-encoding; tracked in ING-412 | main |
| tests/ingest/test_modbus_poller.py | test_reconnect_after_timeout | xfail | flaky against simulator, ING-387 | main |
| tests/quality/test_gap_filler.py | test_linear_fill_across_dst | skip | pending DST fixture (QUAL-118) | main |
| tests/quality/test_outlier_filter.py | test_hampel_window_edges | xfail | known edge-case failure, QUAL-204 | main |

## Summary

- Quarantined tests: 5
- skip: 3
- xfail: 2
- New on release/2.0: 0
- Cleared since main: 0
