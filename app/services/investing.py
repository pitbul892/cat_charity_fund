from datetime import datetime

from sqlalchemy.ext.asyncio import AsyncSession

from app.crud import donation_crud, project_crud
from app.models import CharityProject, Donation


async def investing(obj_in, session: AsyncSession):

    if isinstance(obj_in, Donation):
        # Crud для получения самого раннего проекта
        source_crud_model = project_crud
    elif isinstance(obj_in, CharityProject):
        # Crud для получения самого раннего пожертвования
        source_crud_model = donation_crud
    # Остаток
    remaining_amount = obj_in.full_amount - obj_in.invested_amount
    # Закрытая часть
    invested_amount = obj_in.invested_amount
    # Пока есть остаток
    while remaining_amount > 0:
        # Ранний объект
        earliest_obj = await source_crud_model.get_earliest_object(session)
        if not earliest_obj:
            break
        # Доступный остаток раннего объекта
        available_amount = (
            earliest_obj.full_amount - earliest_obj.invested_amount
        )
        # Если остаток объекта больше или равен доступному остатку
        if remaining_amount >= available_amount:
            # То закрываем доступный объект
            earliest_obj.invested_amount = earliest_obj.full_amount
            earliest_obj.fully_invested = True
            earliest_obj.close_date = datetime.now()
            # Считаем значения для дальнейшего распределения
            remaining_amount -= available_amount
            invested_amount += available_amount
        else:
            # Если остаток объекта меньше чем доступный остаток
            # То закрываем и выходим из цикла
            earliest_obj.invested_amount += remaining_amount
            invested_amount += remaining_amount
            remaining_amount = 0

        await session.commit()
        # await session.refresh(earliest_obj)

    # Считаем и если остаток - 0, то закрываем
    obj_in.invested_amount = invested_amount
    if remaining_amount == 0:
        obj_in.fully_invested = True
        obj_in.close_date = datetime.now()

    await session.commit()
    await session.refresh(obj_in)
