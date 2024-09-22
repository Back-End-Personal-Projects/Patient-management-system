# models/patient.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from . import Base, get_session

class Patient(Base):
    __tablename__ = 'patients'

    patient_id = Column(Integer, primary_key=True)
    _name = Column("name", String, nullable=False)
    _age = Column(Integer)
    sex = Column(String, nullable=False)

    appointments = relationship("Appointment", back_populates="patient")

    def __repr__(self):
        appointment_details = (
            f"Appointment at {', '.join(str(appointment.appointment_time) for appointment in self.appointments)}"
            if self.appointments else "No appointments"
        )
               
        return (f"<Patient(\n"
                f"    name={self.name},\n"
                f"    age={self.age},\n"
                f"    sex={self.sex},\n"
                f"    appointments=[\n"
                f"        {appointment_details}\n"
                f"    ]\n"
                f")>")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Patient name cannot be empty.")
        self._name = value.strip().title() 

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value is not None and (not isinstance(value, int) or value < 0):
            raise ValueError("Age must be a non-negative integer.")
        self._age = value 

    @classmethod
    def get_all(cls):
        session = get_session() 
        try:
            return session.query(cls).all()  
        finally:
            session.close() 