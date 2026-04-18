from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.planner import generate_day_plan
from app.core.types import DayPlan
from app.data.mock_data import LOCATIONS

router = APIRouter()


class PlanRequest(BaseModel):
    locations: list[str]


@router.post("/plan", response_model=DayPlan)
async def plan_day(request: PlanRequest) -> DayPlan:
    if not request.locations:
        raise HTTPException(status_code=400, detail="Provide at least one location.")
    if len(request.locations) > 20:
        raise HTTPException(status_code=400, detail="Maximum 20 locations per request.")
    return await generate_day_plan(request.locations)


@router.get("/locations")
async def list_locations() -> dict:
    return {
        "count": len(LOCATIONS),
        "locations": sorted(LOCATIONS.keys()),
    }
