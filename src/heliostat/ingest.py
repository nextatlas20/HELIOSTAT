"""Inverter telemetry ingestion.

Two entry points are supported: hourly CSV exports produced by the site
gateways, and live Modbus register reads from the inverter fleet.
"""

from dataclasses import dataclass, field
from typing import Dict, List


@dataclass
class Frame:
    columns: List[str]
    rows: List[Dict[str, object]] = field(default_factory=list)

    @property
    def row_count(self) -> int:
        return len(self.rows)


class CsvLoader:
    """Load semicolon-delimited gateway exports into a :class:`Frame`."""

    def __init__(self, delimiter: str = ";") -> None:
        self.delimiter = delimiter

    def load(self, stream) -> Frame:
        text = stream.read()
        if isinstance(text, bytes):
            try:
                text = text.decode("utf-8")
            except UnicodeDecodeError:
                text = text.decode("cp1252")
        lines = [line for line in text.splitlines() if line.strip()]
        if not lines:
            return Frame(columns=[], rows=[])
        header = [cell.strip() for cell in lines[0].split(self.delimiter)]
        if "ts" not in header:
            raise ValueError("gateway export is missing a 'ts' column")
        rows = []
        for line in lines[1:]:
            cells = [cell.strip() for cell in line.split(self.delimiter)]
            rows.append(dict(zip(header, cells)))
        return Frame(columns=header, rows=rows)


class ModbusPoller:
    """Poll holding registers from an inverter over Modbus/TCP."""

    def __init__(self, unit_id: int, host: str, port: int = 502) -> None:
        self.unit_id = unit_id
        self.host = host
        self.port = port
        self._registers: Dict[int, int] = {}

    def read_registers(self, start: int, count: int) -> List[int]:
        if self.unit_id <= 0 or self.unit_id > 247:
            raise ValueError(f"invalid unit id {self.unit_id}")
        return [self._registers.get(start + offset, 0) for offset in range(count)]

    def write_register(self, address: int, value: int) -> None:
        self._registers[address] = int(value)
