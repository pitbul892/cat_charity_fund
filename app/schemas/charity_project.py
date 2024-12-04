from datetime import datetime
from pydantic import BaseModel, Extra, Field, validator, root_validator, PositiveInt
from datetime import timedelta
from typing import Optional


class CharityProjectBase(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str]
    full_amount: Optional[PositiveInt]
    created_date: datetime = Field(default_factory=datetime.now)
    class Config:
        extra = Extra.forbid
        
class CharityProjectCreate(CharityProjectBase):
    name: str = Field(..., min_length=1, max_length=100)
    description: str
    full_amount: PositiveInt

    class Config:
        extra = Extra.forbid
        schema_extra = {
            "example": {
                "name": "string",
                "description": "string",
                "full_amount": 0
            }
        }
class CharityProjectUpdate(CharityProjectBase):
    pass
class CharityProjectDB(CharityProjectBase):
    id:int
    invested_amount: Optional[int] = 0
    fully_invested: Optional[bool] = False
    close_date: Optional[datetime]
    class Config:
        orm_mode = True