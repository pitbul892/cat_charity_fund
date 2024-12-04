from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.schemas.charity_project import CharityProjectDB, CharityProjectCreate
from app.models import CharityProject
from app.crud import project_crud

router = APIRouter()


@router.get('/',
            response_model=list[CharityProjectDB])
async def get_all_projects(
    session: AsyncSession = Depends(get_async_session)
):
    return await project_crud.get_multi(session)

@router.post('/',
             response_model=CharityProjectDB)
async def create_project(
    project: CharityProjectCreate,
    session: AsyncSession = Depends(get_async_session)
):
    #проверку на наличие проекта
    return await project_crud.create(
        project, session
    )
