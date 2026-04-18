"""
Run all 4 test datasets through the day planner and write results to out/.

Usage:
    python scripts/run_tests.py
"""
from __future__ import annotations
import asyncio
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from app.services.planner import generate_day_plan
from app.utils.time_utils import minutes_to_time

TEST_DATASETS: dict[int, dict] = {
    1: {
        "name": "Lower Manhattan",
        "locations": [
            "9/11 Memorial",
            "Battery Park",
            "Charging Bull",
            "Brooklyn Bridge",
            "Wall Street",
        ],
    },
    2: {
        "name": "Midtown",
        "locations": [
            "Times Square",
            "Empire State Building",
            "Rockefeller Center",
            "Bryant Park",
            "Grand Central Terminal",
            "High Line",
        ],
    },
    3: {
        "name": "Museum Mile",
        "locations": [
            "Metropolitan Museum of Art",
            "Guggenheim Museum",
            "American Museum of Natural History",
            "MoMA",
            "Whitney Museum",
        ],
    },
    4: {
        "name": "Brooklyn",
        "locations": [
            "Brooklyn Bridge Park",
            "DUMBO",
            "Prospect Park",
            "Brooklyn Museum",
            "Coney Island",
        ],
    },
}


async def run_test(test_id: int, dataset: dict) -> None:
    sep = "=" * 60
    print(f"\n{sep}")
    print(f"Test {test_id}: {dataset['name']}")
    print(f"Input: {', '.join(dataset['locations'])}")
    print(sep)

    plan = await generate_day_plan(dataset["locations"])

    os.makedirs("out", exist_ok=True)
    output_path = f"out/test{test_id}.json"
    with open(output_path, "w") as f:
        json.dump(plan.model_dump(), f, indent=2)

    print(f"\nRoute  ({plan.total_locations} stops · {plan.total_duration_hours:.1f} h)")
    for item in plan.itinerary:
        transit = ""
        if item.transit_from_prev:
            t = item.transit_from_prev
            transit = f"  ← {t.mode} ({t.time_minutes} min)"
        print(
            f"  {minutes_to_time(item.arrival_time):>9}  {item.location.name}{transit}"
        )

    if plan.skipped_locations:
        print(f"\nSkipped: {', '.join(plan.skipped_locations)}")

    print(f"\nNarrative:\n{plan.summary}")
    print(f"\nSaved → {output_path}")


async def main() -> None:
    for test_id, dataset in TEST_DATASETS.items():
        await run_test(test_id, dataset)


if __name__ == "__main__":
    asyncio.run(main())
