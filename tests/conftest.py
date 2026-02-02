import pytest

from heliostat.ingest import CsvLoader, ModbusPoller
from heliostat.quality import GapFiller, OutlierFilter


@pytest.fixture()
def loader():
    return CsvLoader(delimiter=";")


@pytest.fixture()
def poller():
    return ModbusPoller(unit_id=17, host="127.0.0.1", port=1502)


@pytest.fixture()
def gap_filler():
    return GapFiller(max_gap_minutes=15)


@pytest.fixture()
def median_filter():
    return OutlierFilter(window=5, z_threshold=3.5)
