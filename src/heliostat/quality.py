"""Quality control: gap handling and outlier rejection."""

from typing import Iterable, List, Sequence


class GapFiller:
    """Linearly interpolate short gaps in an irradiance series."""

    def __init__(self, max_gap_minutes: int = 15) -> None:
        self.max_gap_minutes = max_gap_minutes

    def fill(self, values: Sequence[float], step_minutes: int = 5) -> List[float]:
        limit = max(1, self.max_gap_minutes // step_minutes)
        filled = list(values)
        run_start = None
        for index, value in enumerate(filled + [0.0]):
            if value is None:
                if run_start is None:
                    run_start = index
            elif run_start is not None:
                run_length = index - run_start
                if run_length <= limit and 0 < run_start and index < len(filled):
                    before = filled[run_start - 1]
                    after = filled[index]
                    for offset in range(1, run_length + 1):
                        ratio = offset / (run_length + 1)
                        filled[run_start + offset - 1] = before + (after - before) * ratio
                run_start = None
        return filled


class OutlierFilter:
    """Rolling-window Hampel style filter."""

    def __init__(self, window: int = 5, z_threshold: float = 3.0) -> None:
        self.window = window
        self.z_threshold = z_threshold

    def apply(self, values: Iterable[float]) -> List[float]:
        series = list(values)
        half = self.window // 2
        cleaned: List[float] = []
        for index, value in enumerate(series):
            window = series[max(0, index - half): index + half + 1]
            ordered = sorted(window)
            median = ordered[len(ordered) // 2]
            deviation = abs(value - median)
            cleaned.append(None if deviation > self.z_threshold else value)
        return cleaned
