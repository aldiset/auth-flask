import uuid
from sqlalchemy.orm import Session
from werkzeug.security import generate_password_hash

from app.database.models.users import User

class CRUDUser:
    def create(db: Session, data: dict):
        user = db.query(User).filter(User.email == data.get("email")).first()
        if not user:
            user = User(
                public_id = str(uuid.uuid4()),
                name = data.get("name"),
                email = data.get("email"),
                password = generate_password_hash(data.get("password")))
            
            db.add(user)
            db.commit()
            
            return user
        return False

    def get_users(db: Session):
        return db.query(User.public_id, User.name, User.email).all()

    def get_user_by_email(db: Session, email):
        return db.query(User).filter(User.email == email).first()
    
    def get_user_by_public_id(db : Session, public_id: str):
        return db.query(User).filter(User.public_id == public_id).first()