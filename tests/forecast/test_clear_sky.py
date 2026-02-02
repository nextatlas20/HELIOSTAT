import math

from heliostat.forecast import airmass, clear_sky_irradiance


def test_airmass_rounding():
    assert round(airmass(0.0), 3) == 1.0
    assert round(airmass(60.0), 3) == 2.0


def test_linke_turbidity_dst():
    clear = clear_sky_irradiance(30.0, linke_turbidity=3.0)
    hazy = clear_sky_irradiance(30.0, linke_turbidity=5.5)
    assert clear > hazy > 0.0


def test_zenith_beyond_horizon_is_zero():
    assert clear_sky_irradiance(91.5) == 0.0


def test_airmass_is_finite_at_horizon():
    assert math.isfinite(airmass(89.9))
