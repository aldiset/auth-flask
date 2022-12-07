from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from contextlib import contextmanager

from app.config import DATABASE_URL

engine = create_engine(url=DATABASE_URL, connect_args={"check_same_thread": False})
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


@contextmanager
def session_manager():
    session = Session()
    try:
        yield session
    
    except IntegrityError as error:
        print("rollback transaction")
        session.rollback()
        raise error

    except Exception as error:
        print("rollback transaction")
        session.rollback()
        raise error
    finally:
        print("closing session connection")
        session.close()