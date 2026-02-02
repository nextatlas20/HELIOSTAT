import pytest

from heliostat.export import ParquetWriter


def test_writes_header_and_rows():
    writer = ParquetWriter()
    payload = writer.write_rows(["ts", "w_m2"], [["2025-03-01", 412.5]])
    assert payload.splitlines()[0] == "ts,w_m2"


def test_roundtrip_empty_frame():
    writer = ParquetWriter(compression="zstd")
    payload = writer.write_empty(["ts", "w_m2"])
    assert payload.startswith(b"PAR1")
    assert payload.endswith(b"PAR1")


def test_rejects_empty_schema():
    with pytest.raises(ValueError):
        ParquetWriter().write_empty([])
