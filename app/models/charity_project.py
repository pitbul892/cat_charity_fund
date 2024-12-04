from sqlalchemy import Column, Boolean ,DateTime, String, Text, Integer
from sqlalchemy.sql import func
from app.core.db import Base

class CharityProject(Base):
    name = Column(String(100), unique=True, nullable=False)
    description = Column(Text, nullable=False)
    full_amount = Column(Integer)
    invested_amount = Column(Integer, default=0, nullable=False)
    fully_invested = Column(Boolean, default=False)
    create_date = Column(DateTime, default=func.now(), nullable=False)
    close_date = Column(DateTime)