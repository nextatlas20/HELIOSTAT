import pytest


@pytest.mark.slow
@pytest.mark.skip(reason="pending DST fixture (QUAL-118)")
def test_linear_fill_across_dst(gap_filler):
    series = [10.0, 20.0, None, None, 50.0]
    assert gap_filler.fill(series) == [10.0, 20.0, 30.0, 40.0, 50.0]


def test_leaves_long_gaps_untouched(gap_filler):
    series = [1.0, None, None, None, None, 6.0]
    assert gap_filler.fill(series)[1:5] == [None, None, None, None]


def test_keeps_short_gap_endpoints(gap_filler):
    series = [4.0, None, 8.0]
    assert gap_filler.fill(series) == [4.0, 6.0, 8.0]
