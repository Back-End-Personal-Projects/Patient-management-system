from sqlalchemy import Column, Integer, ForeignKey, DateTime, String
from sqlalchemy.orm import relationship
from . import Base, get_session

class Appointment(Base):
    __tablename__ ="appointments"

    appointment_id = Column(Integer, primary_key=True)
    patient_name = Column(String, nullable=False)
    patient_id = Column(Integer, ForeignKey("patients.patient_id"))
    specialist_name = Column(String, nullable=False)
    specialist_id = Column(Integer, ForeignKey("specialists.doc_id"))
    appointment_time = Column(DateTime, nullable=False)
    department_id = Column(Integer, ForeignKey("departments.department_id"))
    

    #Create relationship to other files
    patient = relationship("Patient", back_populates="appointments")
    specialist = relationship("Specialist", back_populates="appointments")
    department = relationship("Department", back_populates="appointments") 


    #Output display
    def __repr__(self):
     return (f"<Appointment(patient_name={self.patient_name}, "
            f"patient_id={self.patient_id}, "
            f"specialist_name={self.specialist_name}, "
            f"appointment_time={self.appointment_time})>")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Patient name cannot be empty.")
        self._name = value.strip().title()

    @classmethod
    def get_all(cls):
        session = get_session() 
        try:
            return session.query(cls).all()  
        finally:
            session.close() 