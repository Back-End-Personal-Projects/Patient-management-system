from sqlalchemy.orm import Session
from lib.models.__init__ import SessionLocal, init_db
from lib.models import Patient, Specialist, Appointment, Department
import datetime

def seed_database():
    """Seed the database with initial data."""
    with SessionLocal() as session:
        try:
            # Create Departments
            departments = [
                Department(name="General"),
                Department(name="Emergencies"),
                Department(name="Gynecology"),
                Department(name="Oncology"),
                Department(name="Urology")
            ]

            session.add_all(departments)
            session.flush()

            # Create Specialists
            specialists = [
                Specialist(name="Dr. Smith", specialty="General Practitioner", department=departments[0]),
                Specialist(name="Dr. Jones", specialty="Gynecologist", department=departments[2]),
                Specialist(name="Dr. Brown", specialty="Oncologist", department=departments[3])
            ]

            session.add_all(specialists)
            session.flush()

            # Create Patients
            patients = [
                Patient(name="Alice", age=30),
                Patient(name="Bob", age=40)
            ]

            session.add_all(patients)
            session.flush()

            # Create Appointments
            appointments = [
                Appointment(patient_id=patients[0].id, specialist_id=specialists[0].id,
                            appointment_time=datetime.datetime(2024, 10, 1, 10, 0)),
                Appointment(patient_id=patients[1].id, specialist_id=specialists[1].id,
                            appointment_time=datetime.datetime(2024, 10, 2, 11, 30))
            ]
           
            session.add_all(appointments)
            session.commit()

            print("Database seeded with initial data.")

        except Exception as e:
            session.rollback()
            print(f"An error occurred: {e}")

if __name__ == '__main__':
    init_db() 
    seed_database()
