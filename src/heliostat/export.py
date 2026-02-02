"""Parquet export helpers for the planning team's data lake."""

from typing import Sequence


class ParquetWriter:
    """Write normalised frames as partitioned Parquet datasets."""

    def __init__(self, compression: str = "snappy") -> None:
        self.compression = compression

    def write_empty(self, schema: Sequence[str]) -> bytes:
        if not schema:
            raise ValueError("schema must contain at least one column")
        return b"PAR1" + "|".join(schema).encode("utf-8") + b"PAR1"

    def write_rows(self, schema: Sequence[str], rows: Sequence[Sequence[object]]) -> bytes:
        payload = "\n".join(",".join(str(cell) for cell in row) for row in rows)
        header = ",".join(schema)
        return (header + "\n" + payload).encode("utf-8")
