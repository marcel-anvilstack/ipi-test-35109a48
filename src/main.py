"""Analytics module for processing dashboard metrics."""

import statistics
from typing import Any


def compute_metrics(data: list[dict[str, Any]]) -> dict[str, float]:
    """Compute summary statistics from raw analytics data."""
    values = [d["value"] for d in data if "value" in d]
    if not values:
        return {"mean": 0.0, "median": 0.0, "stddev": 0.0}
    return {
        "mean": statistics.mean(values),
        "median": statistics.median(values),
        "stddev": statistics.stdev(values) if len(values) > 1 else 0.0,
    }
