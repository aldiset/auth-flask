import uuid
from sqlalchemy.orm import Session
from werkzeug.security import generate_password_hash

from app.database.models import User, UserGroup, Permission, GroupPermission

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
    
class CRUDUserGroup:
    def create(db: Session, data: dict):
        user_group = db.query(UserGroup).filter(UserGroup.user_id == data.get("user_id"), UserGroup.group_id == data.get("group_id")).first()
        if user_group:
            return False
        db.add(**data)
        db.commit()
        return data
    
    def get_user_group_by_id(db: Session, id: int):
        return db.query(UserGroup).filter(UserGroup.id == id).first()
    
    def get_user_groups(db:Session):
        return db.query(UserGroup).all()
    
    def get_user_group_by_user_id(db: Session, user_id):
        return db.query(UserGroup).filter(UserGroup.user_id == user_id).all()
    
    def get_user_group_by_group_id(db: Session, group_id):
        return db.query(UserGroup).filter(UserGroup.group_id == group_id).all()
    
    def get_user_group_by_user_id_group_id(db: Session, user_id: int, group_id: int):
        return  db.query(UserGroup).filter(UserGroup.user_id == user_id, UserGroup.group_id == group_id).all()
    
    def get_user_permission(db: Session, user_id: int):
        group_permission = db.query(UserGroup, GroupPermission).join(GroupPermission, GroupPermission.group_id == UserGroup.group_id).filter(
            UserGroup.user_id == user_id
        ).order_by(GroupPermission.id).all()
        return group_permission


class CRUDGroupPermission:
    def get_group_permission_by_group_id(db: Session, group_id: int):
        return db.query(GroupPermission).filter(GroupPermission.group_id==group_id).all()
