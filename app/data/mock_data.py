from app.core.types import Location

# All times in minutes from midnight.  open=540 → 9 AM, close=1020 → 5 PM.
LOCATIONS: dict[str, Location] = {
    # ── Lower Manhattan ───────────────────────────────────────────────
    "9/11 Memorial": Location(
        name="9/11 Memorial",
        lat=40.7116, lng=-74.0134,
        address="180 Greenwich St, New York, NY 10007",
        open_time=540, close_time=1080, visit_duration=60, category="memorial",
    ),
    "Battery Park": Location(
        name="Battery Park",
        lat=40.7036, lng=-74.0170,
        address="Battery Pl, New York, NY 10004",
        open_time=360, close_time=1320, visit_duration=45, category="park",
    ),
    "Charging Bull": Location(
        name="Charging Bull",
        lat=40.7055, lng=-74.0134,
        address="Broadway & Morris St, New York, NY 10004",
        open_time=0, close_time=1440, visit_duration=20, category="landmark",
    ),
    "Brooklyn Bridge": Location(
        name="Brooklyn Bridge",
        lat=40.7061, lng=-73.9969,
        address="Brooklyn Bridge, New York, NY 10038",
        open_time=0, close_time=1440, visit_duration=40, category="landmark",
    ),
    "Wall Street": Location(
        name="Wall Street",
        lat=40.7074, lng=-74.0113,
        address="Wall St, New York, NY 10005",
        open_time=480, close_time=1080, visit_duration=30, category="landmark",
    ),
    "Staten Island Ferry": Location(
        name="Staten Island Ferry",
        lat=40.7008, lng=-74.0134,
        address="4 Whitehall St, New York, NY 10004",
        open_time=360, close_time=1380, visit_duration=60, category="landmark",
    ),

    # ── Midtown ───────────────────────────────────────────────────────
    "Times Square": Location(
        name="Times Square",
        lat=40.7580, lng=-73.9855,
        address="Manhattan, NY 10036",
        open_time=0, close_time=1440, visit_duration=45, category="landmark",
    ),
    "Empire State Building": Location(
        name="Empire State Building",
        lat=40.7484, lng=-73.9857,
        address="20 W 34th St, New York, NY 10001",
        open_time=480, close_time=1320, visit_duration=90, category="landmark",
    ),
    "Bryant Park": Location(
        name="Bryant Park",
        lat=40.7536, lng=-73.9832,
        address="41st–42nd St, New York, NY 10018",
        open_time=420, close_time=1320, visit_duration=30, category="park",
    ),
    "Rockefeller Center": Location(
        name="Rockefeller Center",
        lat=40.7587, lng=-73.9787,
        address="45 Rockefeller Plaza, New York, NY 10111",
        open_time=480, close_time=1320, visit_duration=60, category="landmark",
    ),
    "Grand Central Terminal": Location(
        name="Grand Central Terminal",
        lat=40.7527, lng=-73.9772,
        address="89 E 42nd St, New York, NY 10017",
        open_time=330, close_time=1380, visit_duration=30, category="landmark",
    ),
    "High Line": Location(
        name="High Line",
        lat=40.7480, lng=-74.0048,
        address="New York, NY 10011",
        open_time=420, close_time=1320, visit_duration=60, category="park",
    ),
    "Chelsea Market": Location(
        name="Chelsea Market",
        lat=40.7424, lng=-74.0060,
        address="75 9th Ave, New York, NY 10011",
        open_time=480, close_time=1320, visit_duration=45, category="market",
    ),

    # ── Museum Mile / Upper East & West ───────────────────────────────
    "Metropolitan Museum of Art": Location(
        name="Metropolitan Museum of Art",
        lat=40.7794, lng=-73.9632,
        address="1000 5th Ave, New York, NY 10028",
        open_time=600, close_time=1020, visit_duration=120, category="museum",
    ),
    "Guggenheim Museum": Location(
        name="Guggenheim Museum",
        lat=40.7830, lng=-73.9590,
        address="1071 5th Ave, New York, NY 10128",
        open_time=600, close_time=1020, visit_duration=90, category="museum",
    ),
    "American Museum of Natural History": Location(
        name="American Museum of Natural History",
        lat=40.7813, lng=-73.9740,
        address="200 Central Park West, New York, NY 10024",
        open_time=600, close_time=1020, visit_duration=120, category="museum",
    ),
    "MoMA": Location(
        name="MoMA",
        lat=40.7614, lng=-73.9776,
        address="11 W 53rd St, New York, NY 10019",
        open_time=600, close_time=1020, visit_duration=120, category="museum",
    ),
    "Whitney Museum": Location(
        name="Whitney Museum",
        lat=40.7396, lng=-74.0089,
        address="99 Gansevoort St, New York, NY 10014",
        open_time=630, close_time=1200, visit_duration=90, category="museum",
    ),
    "Central Park": Location(
        name="Central Park",
        lat=40.7851, lng=-73.9683,
        address="Central Park, New York, NY 10024",
        open_time=360, close_time=1320, visit_duration=60, category="park",
    ),

    # ── Brooklyn ──────────────────────────────────────────────────────
    "Brooklyn Bridge Park": Location(
        name="Brooklyn Bridge Park",
        lat=40.7021, lng=-73.9969,
        address="334 Furman St, Brooklyn, NY 11201",
        open_time=360, close_time=1320, visit_duration=60, category="park",
    ),
    "DUMBO": Location(
        name="DUMBO",
        lat=40.7033, lng=-73.9881,
        address="DUMBO, Brooklyn, NY 11201",
        open_time=0, close_time=1440, visit_duration=45, category="neighborhood",
    ),
    "Prospect Park": Location(
        name="Prospect Park",
        lat=40.6602, lng=-73.9690,
        address="Prospect Park, Brooklyn, NY 11215",
        open_time=300, close_time=1320, visit_duration=60, category="park",
    ),
    "Brooklyn Museum": Location(
        name="Brooklyn Museum",
        lat=40.6712, lng=-73.9636,
        address="200 Eastern Pkwy, Brooklyn, NY 11238",
        open_time=660, close_time=1080, visit_duration=90, category="museum",
    ),
    "Coney Island": Location(
        name="Coney Island",
        lat=40.5755, lng=-73.9707,
        address="Coney Island, Brooklyn, NY 11224",
        open_time=600, close_time=1260, visit_duration=120, category="park",
    ),
    "Industry City": Location(
        name="Industry City",
        lat=40.6572, lng=-74.0101,
        address="220 36th St, Brooklyn, NY 11232",
        open_time=600, close_time=1320, visit_duration=60, category="market",
    ),
}
