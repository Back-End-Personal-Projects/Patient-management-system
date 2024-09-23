from sqlalchemy import Column, Integer, String, func
from sqlalchemy.orm import relationship , joinedload
from . import Base, get_session

class Patient(Base):
    __tablename__ = 'patients'

    patient_id = Column(Integer, primary_key=True,autoincrement=True)
    _name = Column("name", String, nullable=False)
    _age = Column(Integer)
    sex = Column(String, nullable=False)

    appointments = relationship("Appointment", back_populates="patient")

    def __repr__(self):            
        return (f"<Patient(\n"
                f"    name={self.name},\n"
                f"    age={self.age},\n"
                f"    sex={self.sex},\n"
                f")>")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Patient name cannot be empty.")
        self._name = value.strip().title() 

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value is not None and (not isinstance(value, int) or value < 0):
            raise ValueError("Age must be a non-negative integer.")
        self._age = value 

    @property
    def gender(self):
        return self.sex
    
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
            return session.query(cls).filter(cls.patient_id == id_).first()
        finally:
            session.close()

    @classmethod
    def create(cls, name, age, sex):
        session = get_session()
        new_patient = cls()
        new_patient.name = name
        new_patient.age = age
        new_patient.sex = sex
        try:
            session.add(new_patient)
            session.commit()
            return new_patient
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

    @classmethod
    def find_by_name(cls, name):
        session = get_session()
        
        try:
            return session.query(cls).filter(func.lower(cls._name) == name.lower()).all()
        finally:
            session.close()

    @classmethod
    def list_patient(cls):
        session = get_session()
        try:
            patients = session.query(cls).options(joinedload(cls.appointments)).all()
            for patient in patients:
                print(patient)
        finally:
            session.close()