from sqlalchemy.orm import Session
from models.models_init import SessionLocal, init_db
from lib.models import Patient, Specialist, Appointment, Department
import datetime

def seed_database():
    """Seed the database with initial data."""
    with SessionLocal() as session:
        # Create Departments
        general = Department(name="General")
        emergencies = Department(name="Emergencies")
        gynecology = Department(name="Gynecology")
        oncology = Department(name="Oncology")
        urology = Department(name="Urology")

        session.add_all([general, emergencies, gynecology, oncology, urology])
        session.commit()

        # Create Specialists
        specialist1 = Specialist(name="Dr. Smith", specialty="General Practitioner", department=general)
        specialist2 = Specialist(name="Dr. Jones", specialty="Gynecologist", department=gynecology)
        specialist3 = Specialist(name="Dr. Brown", specialty="Oncologist", department=oncology)

        session.add_all([specialist1, specialist2, specialist3])
        session.commit()

        # Create Patients
        patient1 = Patient(name="Alice", age=30)
        patient2 = Patient(name="Bob", age=40)

        session.add_all([patient1, patient2])
        session.commit()

        # Create Appointments
        appointment1 = Appointment(patient_id=patient1.id, specialist_id=specialist1.id, appointment_time=datetime.datetime(2024, 10, 1, 10, 0))
        appointment2 = Appointment(patient_id=patient2.id, specialist_id=specialist2.id, appointment_time=datetime.datetime(2024, 10, 2, 11, 30))

        session.add_all([appointment1, appointment2])
        session.commit()

        print("Database seeded with initial data.")

if __name__ == '__main__':
    init_db() 
    seed_database()  
