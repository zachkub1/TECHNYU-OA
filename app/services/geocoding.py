from app.core.types import Location
from app.data.mock_data import LOCATIONS


def enrich_locations(names: list[str]) -> tuple[list[Location], list[str]]:
    """
    Resolve location names to Location objects.
    Returns (found, unknown_names).
    Falls back to case-insensitive substring match for typos / partial names.
    """
    found: list[Location] = []
    unknown: list[str] = []

    for name in names:
        loc = LOCATIONS.get(name)
        if loc is None:
            # Case-insensitive substring fallback
            matches = [v for k, v in LOCATIONS.items() if name.lower() in k.lower()]
            loc = matches[0] if matches else None

        if loc:
            found.append(loc)
        else:
            unknown.append(name)

    return found, unknown
