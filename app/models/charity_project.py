from sqlalchemy import Column, String, Text

from .base import CharityProjectDonationBase


class CharityProject(CharityProjectDonationBase):
    name = Column(String(100), unique=True, nullable=False)
    description = Column(Text, nullable=False)
