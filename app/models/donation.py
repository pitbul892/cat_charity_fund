from sqlalchemy import Column, ForeignKey, Boolean ,DateTime, String, Text, Integer

from sqlalchemy.sql import func
from app.core.db import Base

class Donation(Base):
    #user_id: 
    comment = Column(Text)
    full_amount = Column(Integer, nullable=False)
    invested_amount = Column(Integer, default=0)
    fully_invested = Column(Boolean, default=False)
    create_date = Column(DateTime, default=func.now(), nullable=False)
    close_date = Column(DateTime)
    user_id = Column(Integer, ForeignKey('user.id'))