from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from models_init import Base

class Appointment(Base):
    __tablename__ =" Appointments"

    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey("patients.id"))
    specialist_id = Column(Integer, ForeignKey("specialist.id"))
    appointment_time = Column(DateTime, nullable=False) 

    #Create relationship to other files
    patient = relationship("Patient", back_populates="appointments")
    specialist = relationship("Specialist", back_populates="appointments")


    #Output display
    def __repr__ (self):
        return f"<Appointment(
        patient_id={self.patient_id},{self.patient_name},
        specialist_id={self.specialist_name},
        appointment_time={self.appointment_time})>"

