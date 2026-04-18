from app.core.types import Location, TransitInfo
from app.utils.distance import haversine


def estimate_travel(a: Location, b: Location) -> TransitInfo:
    """
    Heuristic travel time between two NYC locations.
    Distances < 1 km → walk; 1–5 km → subway; > 5 km → rideshare.
    """
    dist_km = haversine(a.lat, a.lng, b.lat, b.lng)

    if dist_km < 1.0:
        minutes = max(5, int(dist_km / 5.0 * 60))
        return TransitInfo(mode="walk", time_minutes=minutes)
    elif dist_km < 5.0:
        # Subway: ~25 km/h effective speed + 5 min platform wait
        minutes = max(10, int(dist_km / 25.0 * 60) + 5)
        return TransitInfo(mode="subway", time_minutes=minutes)
    else:
        # Rideshare in NYC traffic: ~20 km/h effective
        minutes = max(15, int(dist_km / 20.0 * 60))
        return TransitInfo(mode="rideshare", time_minutes=minutes)
