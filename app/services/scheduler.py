from app.core.types import Location


def is_feasible(arrival: int, location: Location) -> bool:
    """True if we can arrive AND complete the visit within open hours."""
    return location.open_time <= arrival < location.close_time


def adjusted_arrival(arrival: int, location: Location) -> int:
    """If we arrive before opening, wait until open."""
    return max(arrival, location.open_time)
