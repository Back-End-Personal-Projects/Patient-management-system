from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

engine = create_engine('sqlite:///hospital.db',connect_args={"check_same_thread": False}) 

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db(): 
    Base.metadata.create_all(bind=engine)

def get_session():
    return SessionLocal()

from .patient import Patient
from .specialist import Specialist
from .appointment import Appointment
from .department import Department


