# models/department.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from . import Base, get_session


class Department(Base):
    __tablename__ = 'departments'

    department_id = Column(Integer, primary_key=True)
    department_name = Column("name", String, nullable=False) 

    specialists = relationship("Specialist", back_populates="department")
    appointments = relationship("Appointment", back_populates="department")

    def __repr__(self):
     return (f"<Department(name={self.name}, "
             f" department_id={self.department_id})>")


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
