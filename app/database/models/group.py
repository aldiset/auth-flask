from sqlalchemy import Column, String, Integer, Boolean
from app.database import Base

# Database ORMs
class Group(Base):
    __tablename__ = 'group'
    id = Column(Integer, primary_key = True)
    name = Column(String)
    code = Column(String, unique=True)
    is_active = Column(Boolean, default=True)
