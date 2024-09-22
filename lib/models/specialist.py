from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from . import Base, get_session

class Specialist(Base):
    __tablename__ = 'specialists'

    doc_id = Column(Integer, primary_key=True)
    _name = Column(String, nullable=False)
    _specialty = Column(String, nullable=False)
    department_id = Column(Integer, ForeignKey('departments.department_id'))
    
    # Relationships
    appointments = relationship("Appointment", back_populates="specialist")
    department = relationship("Department", back_populates="specialists", foreign_keys=[department_id]) 

    def __repr__(self):
        return (f"<Specialist(name={self._name}, " 
                f"specialty={self.specialty}, " 
                f"department_id={self.department_id})>")
    
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

    @classmethod
    def get_all(cls):
        session = get_session() 
        try:
            return session.query(cls).all()  
        finally:
            session.close() 