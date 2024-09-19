from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from models_init import Base

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