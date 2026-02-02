import io

import pytest


def test_parses_semicolon_delimited_export(loader):
    frame = loader.load(io.StringIO("ts;w_m2\n2025-03-01T10:00:00;412.5\n"))
    assert frame.row_count == 1
    assert frame.columns == ["ts", "w_m2"]


def test_rejects_export_without_timestamp(loader):
    with pytest.raises(ValueError):
        loader.load(io.StringIO("w_m2\n412.5\n"))


def test_handles_cp1252_fallback(loader):
    raw = "ts;site\n2025-03-01T10:00:00;München\n".encode("cp1252")
    frame = loader.load(io.BytesIO(raw))
    assert frame.rows[0]["site"] == "München"


def test_keeps_trailing_empty_cells(loader):
    frame = loader.load(io.StringIO("ts;w_m2;temp_c\n2025-03-01T10:00:00;412.5;\n"))
    assert frame.rows[0]["temp_c"] == ""


def test_normalises_crlf_line_endings(loader):
    frame = loader.load(io.StringIO("ts;w_m2\r\n2025-03-01T10:00:00;412.5\r\n"))
    assert frame.row_count == 1
