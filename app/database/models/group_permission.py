from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

# Database ORMs
class GroupPermission(Base):
    __tablename__ = 'group_permission'
    id = Column(Integer, primary_key = True)
    group_id = Column(Integer, ForeignKey("group.id"))
    permission_id = Column(Integer, ForeignKey("permission.id"))

    group = relationship("Group")
    permission = relationship("Permission")
