from app.core.types import DayPlan
from app.core.config import settings
from app.services.geocoding import enrich_locations
from app.services.optimizer import build_itinerary, two_opt_improve
from app.llm.client import generate_summary


async def generate_day_plan(location_names: list[str]) -> DayPlan:
    locations, unknown = enrich_locations(location_names)

    if not locations:
        return DayPlan(
            itinerary=[],
            total_locations=0,
            total_duration_hours=0.0,
            skipped_locations=unknown,
            summary="No valid locations found.",
        )

    route, skipped = build_itinerary(locations, settings.START_TIME, settings.MAX_HOURS)
    route = two_opt_improve(route, settings.START_TIME, settings.MAX_HOURS)
    all_skipped = skipped + unknown

    total_hours = 0.0
    if route:
        total_hours = round((route[-1].departure_time - route[0].arrival_time) / 60, 2)

    summary = await generate_summary(route)

    return DayPlan(
        itinerary=route,
        total_locations=len(route),
        total_duration_hours=total_hours,
        skipped_locations=all_skipped,
        summary=summary,
    )
