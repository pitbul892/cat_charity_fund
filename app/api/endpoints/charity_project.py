from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.schemas.charity_project import CharityProjectDB, CharityProjectCreate, CharityProjectUpdate
from app.models import CharityProject
from app.crud import project_crud
from ..validators import check_name_duplicate, check_project_before_edit
router = APIRouter()


@router.get('/',
            response_model=list[CharityProjectDB],)
async def get_all_charity_projects(
    session: AsyncSession = Depends(get_async_session)
):
    return await project_crud.get_multi(session)

@router.post('/',
             response_model=CharityProjectDB)
async def create_charity_project(
    project: CharityProjectCreate,
    session: AsyncSession = Depends(get_async_session)
):
    await check_name_duplicate(project.name, session)
    return await project_crud.create(
        project, session
    )

@router.patch(
    '/{project_id}',
    response_model=CharityProjectDB
)
async def update_charity_project(
    project_id: int,
    obj_in: CharityProjectUpdate,
    session: AsyncSession = Depends(get_async_session),
):
    project = await check_project_before_edit(project_id, session)
    if obj_in.name is not None:
        await check_name_duplicate(obj_in.name, session)
    return await project_crud.update(
        project, obj_in, session
    )
    

@router.delete(
    '/{project_id}',
    response_model=CharityProjectDB
)
async def delete_charity_project(
    project_id: int,
    session: AsyncSession = Depends(get_async_session)
):
    project = await check_project_before_edit(project_id, session)
    return await project_crud.remove(project, session)