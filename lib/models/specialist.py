from sqlalchemy import Column, Integer, String, ForeignKey
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
        return (f"Name: {self._name},\n" 
                f"Specialty: {self._specialty}, \n " 
                f"Department_id: {self.department_id}")
    
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

    @classmethod
    def find_by_id(cls, id_):
        session = get_session()
        try:
            return session.query(cls).filter(cls.doc_id == id_).first()
        finally:
            session.close()

    @classmethod
    def create(cls, name, specialty, department_id):
        session = get_session()
        new_specialist = cls(name=name, specialty=specialty, department_id=department_id)
        try:
            session.add(new_specialist)
            session.commit()
            return new_specialist
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
            return session.query(cls).filter(cls._name == name).all()
        finally:
            session.close()