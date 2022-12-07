from sqlalchemy import Column, String, Integer
from app.database import Base

# Database ORMs
class Permission(Base):
    __tablename__ = 'permission'
    id = Column(Integer, primary_key = True)
    name = Column(String)
    code = Column(String, uniqe=True)
    is_active = Column(bool, default=True)
