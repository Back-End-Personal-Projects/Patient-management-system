from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.models_init import Base

class Patient(Base):
    __tablename__ = "Patients"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer)
    email = Column(String, nullable=False)


    #one to many rship with appointments
    appointments = relationship("Appointmant", back_populates="patient")


    def __repr__(self):
        return f"<Patient(
        name={self.name},
        age={self.age},
        email={self.email})
        >"