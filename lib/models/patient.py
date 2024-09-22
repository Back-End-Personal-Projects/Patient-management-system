# models/patient.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.__init__ import Base

class Patient(Base):
    __tablename__ = 'patients'

    id = Column(Integer, primary_key=True)
    _name = Column("name", String, nullable=False)
    age = Column(Integer)

    appointments = relationship("Appointment", back_populates="patient")

    def __repr__(self):
        return f"<Patient(name={self.name}, age={self.age})>"

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
