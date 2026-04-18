import anthropic
from app.core.config import settings
from app.core.types import ItineraryItem
from app.llm.prompts import build_itinerary_prompt
from app.utils.time_utils import minutes_to_time


async def generate_summary(itinerary: list[ItineraryItem]) -> str:
    if not itinerary:
        return "No stops scheduled."

    if not settings.ANTHROPIC_API_KEY:
        return _fallback_summary(itinerary)

    try:
        client = anthropic.AsyncAnthropic(api_key=settings.ANTHROPIC_API_KEY)
        message = await client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=1024,
            messages=[{"role": "user", "content": build_itinerary_prompt(itinerary)}],
        )
        return message.content[0].text
    except Exception:
        return _fallback_summary(itinerary)


def _fallback_summary(itinerary: list[ItineraryItem]) -> str:
    lines = [f"Your {len(itinerary)}-stop NYC day plan:\n"]
    for i, item in enumerate(itinerary, 1):
        transit = ""
        if item.transit_from_prev:
            t = item.transit_from_prev
            transit = f"  ← {t.mode} ({t.time_minutes} min)"
        lines.append(
            f"  {i}. {item.location.name}"
            f"  |  {minutes_to_time(item.arrival_time)} – {minutes_to_time(item.departure_time)}"
            + transit
        )
    return "\n".join(lines)
