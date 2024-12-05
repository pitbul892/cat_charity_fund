from typing import Optional

from app.crud.base import CRUDBase
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models import Donation

class CRUDDonation(CRUDBase):
    pass