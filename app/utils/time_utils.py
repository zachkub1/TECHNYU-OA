def minutes_to_time(minutes: int) -> str:
    """Convert minutes-from-midnight to 12-hour clock string, e.g. 540 → '9:00 AM'."""
    h, m = divmod(minutes, 60)
    period = "AM" if h < 12 else "PM"
    display = h % 12 or 12
    return f"{display}:{m:02d} {period}"
