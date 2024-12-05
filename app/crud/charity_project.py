from typing import Optional

from app.crud.base import CRUDBase
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models import CharityProject

class CRUDCharityProject(CRUDBase):
    async def get_project_by_name(
            self,
            project_name: str,
            session: AsyncSession
    ) -> Optional[int]:
        db_project_id = await session.execute(
            select(CharityProject.id).where(
                CharityProject.name == project_name
            )
        )
        return db_project_id.scalars().first()   




