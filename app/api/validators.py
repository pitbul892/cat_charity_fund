from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.models import CharityProject
from app.crud import project_crud

async def check_project_before_edit(
        project_id: int,
        session: AsyncSession,
) -> CharityProject:
    project = await project_crud.get(project_id, session)
    if not project:
        raise HTTPException(
            status_code=404,
            detail='Проект не найден!'
        )
    return project

async def check_name_duplicate(
        project_name: str,
        session: AsyncSession
) -> None:
    project_id = await project_crud.get_project_by_name(project_name, session)
    if project_id is not None:
        raise HTTPException(
            status_code=422,
            detail='Проект с таким именем уже существует!',
        )