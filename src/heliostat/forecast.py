"""Clear-sky irradiance models and forecast skill scoring."""

import math
from typing import Sequence


def airmass(zenith_degrees: float) -> float:
    """Kasten-Young relative airmass."""
    zenith = math.radians(zenith_degrees)
    return 1.0 / (math.cos(zenith) + 0.50572 * (96.07995 - zenith_degrees) ** -1.6364)


def clear_sky_irradiance(zenith_degrees: float, linke_turbidity: float = 3.0) -> float:
    """Simplified Linke turbidity clear-sky global horizontal irradiance."""
    if zenith_degrees >= 90:
        return 0.0
    return 1361.0 * math.cos(math.radians(zenith_degrees)) * math.exp(
        -0.09 * linke_turbidity * airmass(zenith_degrees)
    )


def skill_score(observed: Sequence[float], forecast: Sequence[float]) -> float:
    """One minus the ratio of forecast error to persistence error."""
    if len(observed) != len(forecast):
        raise ValueError("observed and forecast series differ in length")
    persistence_error = sum(abs(observed[i] - observed[i - 1]) for i in range(1, len(observed)))
    forecast_error = sum(abs(observed[i] - forecast[i]) for i in range(len(observed)))
    if persistence_error == 0:
        return 0.0
    return 1.0 - forecast_error / persistence_error
