"""
Plan a day for any set of locations.

Usage:
    python scripts/plan.py "Times Square" "MoMA" "Central Park" "High Line"
    python scripts/plan.py --list          # show all available locations
"""
from __future__ import annotations
import asyncio
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from app.services.planner import generate_day_plan
from app.utils.time_utils import minutes_to_time


async def main(locations: list[str]) -> None:
    print(f"\nPlanning: {', '.join(locations)}\n")

    plan = await generate_day_plan(locations)

    if not plan.itinerary:
        print("No valid route found.")
        if plan.skipped_locations:
            print(f"Unknown locations: {', '.join(plan.skipped_locations)}")
        return

    print(f"Route  ({plan.total_locations} stops · {plan.total_duration_hours:.1f} h)")
    print("-" * 50)
    for item in plan.itinerary:
        transit = ""
        if item.transit_from_prev:
            t = item.transit_from_prev
            transit = f"  ← {t.mode} ({t.time_minutes} min)"
        print(f"  {minutes_to_time(item.arrival_time):>9}  {item.location.name}{transit}")

    if plan.skipped_locations:
        print(f"\nSkipped (didn't fit): {', '.join(plan.skipped_locations)}")

    print(f"\n{plan.summary}")

    os.makedirs("out", exist_ok=True)
    slug = "_".join(locations[0].lower().split())[:20]
    path = f"out/plan_{slug}.json"
    with open(path, "w") as f:
        json.dump(plan.model_dump(), f, indent=2)
    print(f"\nSaved → {path}")


def list_locations() -> None:
    from app.data.mock_data import LOCATIONS
    print(f"\n{len(LOCATIONS)} available locations:\n")
    by_category: dict[str, list[str]] = {}
    for loc in LOCATIONS.values():
        by_category.setdefault(loc.category, []).append(loc.name)
    for category, names in sorted(by_category.items()):
        print(f"  [{category}]")
        for name in sorted(names):
            print(f"    {name}")


if __name__ == "__main__":
    args = sys.argv[1:]

    if not args or args[0] in ("-h", "--help"):
        print(__doc__)
        sys.exit(0)

    if args[0] == "--list":
        list_locations()
        sys.exit(0)

    asyncio.run(main(args))
