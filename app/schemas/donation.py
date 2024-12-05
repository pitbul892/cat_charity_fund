from datetime import datetime
from pydantic import BaseModel, Extra, Field, validator, root_validator, PositiveInt
from datetime import timedelta
from typing import Optional


class DonationBase(BaseModel):
    full_amount: PositiveInt
    comment: Optional[str]
    class Config:
        extra = Extra.forbid
class DonationCreate(DonationBase):
        pass

class DonationDB(DonationBase):
    id: int
    create_date: Optional[datetime]
    invested_amount: Optional[int] = 0
    fully_invested: Optional[bool] = False
    close_date: Optional[datetime]
    class Config:
        orm_mode = True