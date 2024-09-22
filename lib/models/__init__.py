from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

engine = create_engine('sqlite:///hospital.db',connect_args={"check_same_thread": False}) 

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    from .department import Department
    from .specialist import Specialist
    from .patient import Patient
    from .appointment import Appointment
    


    Base.metadata.create_all(bind=engine)
    
