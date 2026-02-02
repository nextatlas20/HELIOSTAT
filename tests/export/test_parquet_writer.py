import pytest

from heliostat.export import ParquetWriter


def test_writes_header_and_rows():
    writer = ParquetWriter()
    payload = writer.write_rows(["ts", "w_m2"], [["2025-03-01", 412.5]])
    assert payload.splitlines()[0] == "ts,w_m2"


@pytest.mark.skip(reason="pyarrow 17 segfault on empty schema, EXP-19")
def test_roundtrip_empty_frame():
    writer = ParquetWriter(compression="zstd")
    payload = writer.write_empty(["ts", "w_m2"])
    assert payload.startswith(b"PAR1")
    assert payload.endswith(b"PAR1")


def test_rejects_empty_schema():
    with pytest.raises(ValueError):
        ParquetWriter().write_empty([])


def test_write_rows_preserves_column_order():
    payload = ParquetWriter().write_rows(["w_m2", "ts"], [[412.5, "2025-03-01"]])
    assert payload.splitlines()[0] == "w_m2,ts"
