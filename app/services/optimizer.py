from __future__ import annotations
from app.core.types import Location, ItineraryItem, TransitInfo
from app.services.transit import estimate_travel
from app.services.scheduler import is_feasible, adjusted_arrival


def build_itinerary(
    locations: list[Location],
    start_time: int,
    max_hours: int,
) -> tuple[list[ItineraryItem], list[str]]:
    """
    Greedy nearest-neighbor route builder with time-window enforcement.
    Returns (route, skipped_names).
    """
    if not locations:
        return [], []

    max_time = start_time + max_hours * 60
    remaining = list(locations)
    route: list[ItineraryItem] = []
    skipped: list[str] = []

    first = remaining.pop(0)
    arr = adjusted_arrival(start_time, first)
    dep = arr + first.visit_duration
    if dep > max_time or not is_feasible(arr, first):
        skipped.append(first.name)
    else:
        route.append(ItineraryItem(location=first, arrival_time=arr, departure_time=dep))

    while remaining:
        if not route:
            skipped.extend(loc.name for loc in remaining)
            break

        current_time = route[-1].departure_time
        current_loc = route[-1].location
        best_loc: Location | None = None
        best_transit: TransitInfo | None = None
        best_arrival = 0
        best_cost = float("inf")

        for candidate in remaining:
            transit = estimate_travel(current_loc, candidate)
            arrival = adjusted_arrival(current_time + transit.time_minutes, candidate)

            if not is_feasible(arrival, candidate):
                continue
            if arrival + candidate.visit_duration > max_time:
                continue

            if transit.time_minutes < best_cost:
                best_loc = candidate
                best_transit = transit
                best_arrival = arrival
                best_cost = transit.time_minutes

        if best_loc is None:
            skipped.extend(loc.name for loc in remaining)
            break

        route.append(ItineraryItem(
            location=best_loc,
            arrival_time=best_arrival,
            departure_time=best_arrival + best_loc.visit_duration,
            transit_from_prev=best_transit,
        ))
        remaining.remove(best_loc)

    return route, skipped


def _total_travel_time(order: list[Location]) -> int:
    return sum(
        estimate_travel(order[i], order[i + 1]).time_minutes
        for i in range(len(order) - 1)
    )


def two_opt_improve(
    route: list[ItineraryItem],
    start_time: int,
    max_hours: int,
) -> list[ItineraryItem]:
    """
    2-opt local search over the raw travel-time objective.
    Keeps the first location fixed (natural start point).
    Only applies the improvement if no locations are lost to time-window violations.
    """
    if len(route) <= 2:
        return route

    best = [item.location for item in route]
    best_time = _total_travel_time(best)
    improved = True

    while improved:
        improved = False
        for i in range(1, len(best) - 1):       # keep index 0 fixed
            for j in range(i + 1, len(best)):
                candidate = best[:i] + best[i : j + 1][::-1] + best[j + 1 :]
                t = _total_travel_time(candidate)
                if t < best_time:
                    best = candidate
                    best_time = t
                    improved = True

    if best == [item.location for item in route]:
        return route

    new_route, _ = build_itinerary(best, start_time, max_hours)
    return new_route if len(new_route) >= len(route) else route
