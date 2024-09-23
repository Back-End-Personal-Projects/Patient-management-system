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
     return (f"patient_name: {self.patient_name}, "
            f"patient_id: {self.patient_id}, "
            f"specialist_name: {self.specialist_name}, "
            f"appointment_time:{self.appointment_time}")

  
    @classmethod
    def get_all(cls):
        session = get_session() 
        try:
            return session.query(cls).all()  
        finally:
            session.close() 

    @classmethod
    def find_by_id(cls, id_):
        session = get_session()
        try:
            return session.query(cls).filter(cls.appointment_id == id_).first()
        finally:
            session.close()

    @classmethod
    def find_by_patient_name(cls, name):
        session = get_session()
        try:
            return session.query(cls).filter(cls.patient_name == name).all()
        finally:
            session.close()

    @classmethod
    def find_by_specialist_name(cls, name):
        session = get_session()
        try:
            return session.query(cls).filter(cls.specialist_name == name).all()
        finally:
            session.close()

    @classmethod
    def find_by_date(cls, date_):
        session = get_session()
        try:
            return session.query(cls).filter(cls.appointment_time == date_).all()
        finally:
            session.close()

    @classmethod
    def create(cls, patient_name, patient_id, specialist_name, specialist_id, appointment_time, department_id):
        session = get_session()
        new_appointment = cls(
            patient_name=patient_name,
            patient_id=patient_id,
            specialist_name=specialist_name,
            specialist_id=specialist_id,
            appointment_time=appointment_time,
            department_id=department_id
        )
        try:
            session.add(new_appointment)
            session.commit()
            return new_appointment
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    def update(self):
        session = get_session()
        try:
            session.merge(self)  
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    def delete(self):
        session = get_session()
        try:
            session.delete(self)
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()      