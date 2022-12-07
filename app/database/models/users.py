from sqlalchemy import Column, String, Integer
from app.database import Base

# Database ORMs
class User(Base):
	__tablename__ = 'user'
	id = Column(Integer, primary_key = True)
	public_id = Column(String(50), unique = True)
	name = Column(String(100))
	email = Column(String(70), unique = True)
	password = Column(String(80))