import click
from sqlalchemy.orm import Session
from models.models_init import SessionLocal, init_db
from lib.models import Patient, Specialist, Appointment, Department

@click.group()
def cli():
    """Hospital Management System CLI"""
    pass

@cli.command()
def initdb():
    """Initialize the database."""
    init_db()
    click.echo("Database initialized.")

@cli.command()
@click.argument('name')
@click.argument('age', type=int)
def add_patient(name, age):
    """Add a new patient."""
    with SessionLocal() as session:
        patient = Patient(name=name, age=age)
        session.add(patient)
        session.commit()
        click.echo(f"Patient {name} added.")

@cli.command()
@click.argument('name')
@click.argument('specialty')
@click.argument('department_name')
def add_specialist(name, specialty, department_name):
    """Add a new specialist."""
    with SessionLocal() as session:
        # Check if department exists, or create it
        department = session.query(Department).filter_by(name=department_name).first()
        if not department:
            department = Department(name=department_name)
            session.add(department)
        
        specialist = Specialist(name=name, specialty=specialty, department=department)
        session.add(specialist)
        session.commit()
        click.echo(f"Specialist {name} added.")

@cli.command()
@click.argument('patient_id', type=int)
@click.argument('specialist_id', type=int)
@click.argument('appointment_time')
def add_appointment(patient_id, specialist_id, appointment_time):
    """Add a new appointment."""
    with SessionLocal() as session:
        appointment = Appointment(patient_id=patient_id, specialist_id=specialist_id, appointment_time=appointment_time)
        session.add(appointment)
        session.commit()
        click.echo(f"Appointment scheduled for patient {patient_id} with specialist {specialist_id}.")

if __name__ == '__main__':
    cli()
