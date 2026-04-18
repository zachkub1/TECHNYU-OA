from __future__ import annotations
from pydantic import BaseModel
from typing import Optional


class Location(BaseModel):
    name: str
    lat: float
    lng: float
    address: str
    open_time: int       # minutes from midnight
    close_time: int
    visit_duration: int  # minutes
    category: str = "landmark"


class TransitInfo(BaseModel):
    mode: str            # "walk" | "subway" | "rideshare"
    time_minutes: int


class ItineraryItem(BaseModel):
    location: Location
    arrival_time: int    # minutes from midnight
    departure_time: int
    transit_from_prev: Optional[TransitInfo] = None


class DayPlan(BaseModel):
    itinerary: list[ItineraryItem]
    total_locations: int
    total_duration_hours: float
    skipped_locations: list[str]
    summary: str
