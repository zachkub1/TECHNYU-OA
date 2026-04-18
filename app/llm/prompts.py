from app.core.types import ItineraryItem
from app.utils.time_utils import minutes_to_time


def build_itinerary_prompt(itinerary: list[ItineraryItem]) -> str:
    stops: list[str] = []
    for i, item in enumerate(itinerary, 1):
        transit_line = ""
        if item.transit_from_prev:
            t = item.transit_from_prev
            transit_line = f"\n   Getting there: {t.mode} (~{t.time_minutes} min)"

        stops.append(
            f"{i}. {item.location.name} [{item.location.category}]"
            f"\n   {minutes_to_time(item.arrival_time)} – {minutes_to_time(item.departure_time)}"
            + transit_line
        )

    stops_text = "\n".join(stops)

    return f"""You are a knowledgeable NYC tour guide. \
Write an engaging, practical day-trip narrative for this optimized itinerary.

For each stop include:
- A 1–2 sentence description of what makes it worth visiting
- Exact arrival and departure times
- How to get there from the previous stop (mode + time)
- One practical tip (best entrance, must-see highlight, nearby food option)

Keep the tone friendly and NYC-specific. Under 450 words total.

Itinerary:
{stops_text}

Write the narrative now:"""
