import sys

import pytest


@pytest.mark.xfail(reason="known edge-case failure, QUAL-204")
def test_hampel_window_edges(median_filter):
    series = [100.0, 101.0, 99.0, 100.0, 900.0]
    assert median_filter.apply(series)[-1] is None


# @pytest.mark.skip(reason="disabled while QUAL-190 is investigated")
def test_rolling_median_window(median_filter):
    series = [5.0, 5.0, 5.0, 40.0, 5.0]
    assert median_filter.apply(series)[3] is None


@pytest.mark.skipif(sys.platform == "win32", reason="serial port unavailable on CI runners")
def test_reads_from_serial_device(median_filter):
    assert median_filter.apply([1.0, 2.0, 3.0]) == [1.0, 2.0, 3.0]
