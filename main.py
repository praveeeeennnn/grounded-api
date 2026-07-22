import calendar
from pydantic import BaseModel

class ProrateRequest(BaseModel):
    old_price: float
    new_price: float
    year: int
    month: int
    upgrade_day: int


@app.post("/prorate")
async def prorate(req: ProrateRequest):
    # Actual number of days in the month
    days_in_month = calendar.monthrange(req.year, req.month)[1]

    # Inclusive of the upgrade day
    days_remaining = days_in_month - req.upgrade_day + 1

    # v2 formula
    charge = (req.new_price - req.old_price) * (
        days_remaining / days_in_month
    )

    return {
        "charge": round(charge, 2)
    }
