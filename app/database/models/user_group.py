from sqlalchemy import Column, String, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.database import Base

# Database ORMs
class UserGroup(Base):
    __tablename__ = 'user_group'
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey("user.id"))
    group_id = Column(Integer, ForeignKey("group.id"))
    is_active = Column(Boolean, default=True)

    user = relationship("User")
    group = relationship("Group")
