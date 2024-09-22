# models/department.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models. __init__ import Base

class Department(Base):
    __tablename__ = 'departments'

    id = Column(Integer, primary_key=True)
    _name = Column("name", String, nullable=False) 

    specialists = relationship("Specialist", back_populates="department")
    appointments = relationship("Appointment", back_populates="department")

    def __repr__(self):
        return f"<Department(name={self.name})>"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Department name cannot be empty.")
        self._name = value.strip().title() 
