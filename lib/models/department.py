from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models_init import Base

class Department(Base):
    __tablename__ = 'Departments'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    # Relationship to specialists
    specialists = relationship("Specialist", back_populates="department")
    appointment = relationship("Appointment", back_populates="department")

    def __repr__(self):
        return f"<Department(name={self.name})>"
