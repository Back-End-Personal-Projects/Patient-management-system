from sqlalchemy import Column, Integer, ForeignKey, DateTime, String
from sqlalchemy.orm import relationship
from models.__init__ import Base

class Appointment(Base):
    __tablename__ ="appointments"

    id = Column(Integer, primary_key=True)
    patient_name = Column(String, nullable=False)
    patient_id = Column(Integer, ForeignKey("patients.id"))
    specialist_id = Column(Integer, ForeignKey("specialists.id"))
    appointment_time = Column(DateTime, nullable=False)
    

    #Create relationship to other files
    patient = relationship("Patient", back_populates="appointments")
    specialist = relationship("Specialist", back_populates="appointments")
    department = relationship("Department", back_populates="appointments") 


    #Output display
    def __repr__(self):
     return (f"<Appointment(patient_name={self.patient_name}, "
            f"patient_id={self.patient_id}, "
            f"specialist_id={self.specialist_id}, "
            f"appointment_time={self.appointment_time})>")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Patient name cannot be empty.")
        self._name = value.strip().title()
