from sqlalchemy import Column, Integer, ForeignKey, String, func
from sqlalchemy.orm import relationship, joinedload
from sqlalchemy import DateTime
from .import Base, get_session
from .patient import Patient
from .specialist import Specialist
from .department import Department

class Appointment(Base):
    __tablename__ ="appointments"

    appointment_id = Column(Integer, primary_key=True, autoincrement=True)
    patient_id = Column(Integer, ForeignKey("patients.patient_id"))
    #patient_name = Column(String, nullable=False)
    specialist_id = Column(Integer, ForeignKey("specialists.doc_id"))
    #specialist_name = Column(String, nullable=False)
    appointment_time = Column(DateTime, nullable=False)
    department_id = Column(Integer, ForeignKey("departments.department_id"))
    

    #Create relationship to other files
    patient = relationship("Patient", back_populates="appointments")
    specialist = relationship("Specialist", back_populates="appointments")
    department = relationship("Department", back_populates="appointments") 


    #Output display
    def __repr__(self):
        patient_name = self.patient.name if self.patient else 'N/A'
        specialist_name = self.specialist.name if self.specialist else 'N/A'
        return (f"appointment_id: {self.appointment_id}, "
                f"patient_name: {patient_name}, "
                f"specialist_name: {specialist_name}, "
                f"appointment_time: {self.appointment_time}")
    # def __repr__(self):
    #     return (f"appointment_id: {self.appointment_id}, "
    #             f"patient_name: {self.patient.name if self.patient else 'N/A'}, "
    #             f"specialist_name: {self.specialist._name if self.specialist else 'N/A'}, "
    #             f"appointment_time: {self.appointment_time}")

    @property
    def name(self):
     return self._name
    @classmethod
    def get_all(cls):
        session = get_session() 
        try:
            return session.query(cls).options(joinedload(cls.patient), 
                                           joinedload(cls.specialist), 
                                           joinedload(cls.department)).all()
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
           return session.query(cls).join(cls.patient).filter(func.lower(Patient._name) == name.lower()).options(joinedload(cls.patient), joinedload(cls.specialist)).all()
        finally:
            session.close()

    @classmethod
    def find_by_specialist_name(cls, name):
        session = get_session()
        try:
             return (
            session.query(cls)
            .join(cls.specialist)
            .filter(func.lower(Specialist._name) == name.lower())
            .options(joinedload(cls.patient), joinedload(cls.specialist))  # Eager load
            .all()
        )
        finally:
            session.close()

    @classmethod
    def find_by_date(cls, date_):
        session = get_session()
        try:
            return session.query(cls).options(joinedload(cls.patient), joinedload(cls.specialist)).filter(func.date(cls.appointment_time) == date_).all()
        finally:
            session.close()

    @classmethod
    def create(cls, patient_id, specialist_id, appointment_time, department_id):
        session = get_session()
        
        # Fetch the patient
        patient = session.query(Patient).filter(Patient.patient_id == patient_id).first()
        if not patient:
            raise ValueError(f"Patient with ID {patient_id} does not exist.")

        # Fetch the specialist
        specialist = session.query(Specialist).filter(Specialist.doc_id == specialist_id).first()
        if not specialist:
            raise ValueError(f"Specialist with ID {specialist_id} does not exist.")
        
        # Fetch the department
        department = session.query(Department).filter(Department.department_id == department_id).first()
        if not department:
            raise ValueError(f"Department with ID {department_id} does not exist.")

        # Create the new appointment
        new_appointment = cls(
            patient_id=patient_id,
            specialist_id=specialist_id,
            appointment_time=appointment_time,
            department_id=department_id,
              
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