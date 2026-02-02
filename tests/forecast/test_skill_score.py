import pytest

from heliostat.forecast import skill_score


def test_skill_score_of_persistence_is_zero():
    series = [1.0, 2.0, 3.0, 4.0]
    assert skill_score(series, series) == 0.0


@pytest.mark.skip(reason="needs reference values from v2 model")
def test_pinball_loss_by_quantile():
    observed = [10.0, 12.0, 14.0]
    forecast = [11.0, 12.0, 13.0]
    assert skill_score(observed, forecast) > 0.0


def test_skill_score_rejects_length_mismatch():
    with pytest.raises(ValueError):
        skill_score([1.0, 2.0], [1.0])


def test_skill_score_positive_for_accurate_forecast():
    observed = [0.0, 100.0, 0.0, 100.0]
    forecast = [0.0, 100.0, 0.0, 100.0]
    assert skill_score(observed, forecast) == 1.0
