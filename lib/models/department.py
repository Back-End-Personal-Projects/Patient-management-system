from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from . import Base, get_session


class Department(Base):
    __tablename__ = 'departments'

    department_id = Column(Integer, primary_key=True, autoincrement=True)
    department_name = Column("name", String, nullable=False) 

    specialists = relationship("Specialist", back_populates="department")
    appointments = relationship("Appointment", back_populates="department")

    def __repr__(self):
     return (f"Department_name: {self.name}, "
             f" Department_id: {self.department_id}")


    @property
    def name(self):
        return self.department_name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Department name cannot be empty.")
        self.department_name = value.strip().title() 

    @classmethod
    def get_all(cls):
        session = get_session() 
        try:
            return session.query(cls).all()  
        finally:
            session.close()  

    @classmethod
    def find_by_name(cls, name):
        session = get_session()
        try:
            return session.query(cls).filter(cls.department_name == name).first()
        finally:
            session.close()

    @classmethod
    def find_by_id(cls, id_):
        session = get_session()
        try:
            return session.query(cls).filter(cls.department_id == id_).first()
        finally:
            session.close()

    @classmethod
    def create(cls, name):
        session = get_session()
        new_department = cls(department_name=name)
        try:
            session.add(new_department)
            session.commit()
            return new_department
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

    
