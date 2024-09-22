from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from . import Base

class Specialist(Base):
    __tablename__ = 'specialists'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    specialty = Column(String, nullable=False)
    department_id = Column(Integer, ForeignKey('departments.id'))  

    # Relationships
    appointments = relationship("Appointment", back_populates="specialist")
    department = relationship("Department", back_populates="specialists") 

    def __repr__(self):
        return f"<Specialist(name={self.name}, specialty={self.specialty})>"
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Specialist name cannot be empty.")
        self._name = value.strip().title()

    @property
    def specialty(self):
        return self._specialty

    @specialty.setter
    def specialty(self, value):
        if not value:
            raise ValueError("Specialty cannot be empty.")
        self._specialty = value.strip().title()