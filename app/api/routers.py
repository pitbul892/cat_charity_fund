from fastapi import APIRouter
from .endpoints import project_router, donation_router

main_router = APIRouter()

main_router.include_router(
    project_router, prefix='/charity_project',
    tags = ['charity_project']
)
main_router.include_router(
    donation_router, prefix='/donation',
    tags = ['donationt']
)