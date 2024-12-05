from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.schemas.donation import DonationDB, DonationCreate
from app.schemas.charity_project import CharityProjectDB, CharityProjectCreate, CharityProjectUpdate
from app.models import CharityProject
from app.crud import project_crud, donation_crud
from ..validators import check_name_duplicate, check_project_before_edit
router = APIRouter()

@router.get('/',
            response_model=list[DonationDB],)
async def get_all_donations(
    session: AsyncSession = Depends(get_async_session)
):
    return await donation_crud.get_multi(session)

@router.post('/',
             response_model=DonationDB,
             response_model_exclude={'invested_amount', 'fully_invested','close_date'})
async def create_donation(
    donation: DonationCreate,
    session: AsyncSession = Depends(get_async_session)
):

    return await donation_crud.create(
        donation, session
    )
# @router.get('/my',
#             response_model=DonationDB,
#             response_model_exclude={'invested_amount'})
# async def get_all_donation(
#     session: AsyncSession = Depends(get_async_session)
# ):
#     return await project_crud.get_multi(session)