from lib.models.department import Department
from lib.models.specialist import Specialist
from lib.models.patient import Patient
from lib.models.appointment import Appointment
from datetime import datetime
from lib.models import SessionLocal

session = SessionLocal()

def exit_program():
    print("Goodbye!")
    exit()

def list_departments():
    departments = Department.get_all()
    for department in departments:
        print(department)

def find_department_by_name():
    name = input("Enter the department's name: ")
    department = Department.find_by_name(name)
    print(department) if department else print(f'{name} Department not found')

def find_department_by_id():
    id_ = input("Enter the department's id: ")
    department = Department.find_by_id(id_)
    print(department) if department else print(f'Department not found')

def create_department():
    name = input("Enter the department's name: ")
       
    try:      
        # Create a new department instance
        department = Department(name=name)

        # Add to session and commit
        session.add(department)
        session.commit()
        print(f'Success:  {department.name} department was created.')
    except ValueError as ve:
        print("Error: ", ve)
    except Exception as exc:
        session.rollback()  # Roll back in case of an error
        print("Error creating department: ", exc)


def update_department():
    id_ = input("Enter the department's id: ")
    department = Department.find_by_id(id_)
    if department:
        try:
            name = input("Enter the department's new name: ")
            department.name = name
            department.update()
            print(f'Success: {department}')
        except Exception as exc:
            print("Error updating department: ", exc)
    else:
        print(f'Department {id_} not found')

def delete_department():
    id_ = input("Enter the department's id: ")
    department = Department.find_by_id(id_)
    if department:
        department.delete()
        print(f'Department {id_} deleted')
    else:
        print(f'Department {id_} not found')

# Specialist Functions

def list_specialist():
    specialists = Specialist.get_all()
    for specialist in specialists:
        print(specialist)

def find_specialist_by_name():
    name = input("Enter the specialist's name: ")
    specialist = Specialist.find_by_name(name)
    print(specialist) if specialist else print(f'Specialist {name} not found')

def find_specialist_by_id():
    id_ = input("Enter the specialist's id: ")
    specialist = Specialist.find_by_id(id_)
    print(specialist) if specialist else print(f'Specialist {id_} not found')

def create_specialist():
    name = input("Enter the specialist's name: ")
    specialty = input("Enter the specialist's specialty: ")
        
    try:
        department_id = int(input("Enter the department's id: "))
        if not Department.find_by_id(department_id):
            print(f"Error: Department ID {department_id} does not exist.")
            return
    except ValueError:
        print("Error: Department ID must be an integer.")
        return
    
    try:      
        # Create a new specialist instance
        specialist = Specialist(name=name,specialty=specialty, department_id=department_id)

        # Add to session and commit
        session.add(specialist)
        session.commit()
        print(f'Success: Specialist {specialist.name} was created.')
    except ValueError as ve:
        print("Error: ", ve)
    except Exception as exc:
        session.rollback()  # Roll back in case of an error
        print("Error creating specialist: ", exc)

def update_specialist():
    id_ = input("Enter the specialist's id: ")
    specialist = Specialist.find_by_id(id_)
    if specialist:
        try:
            name = input("Enter the specialist's new name: ")
            specialty=input("Enter the new specialty: ")
            department_id = input("Enter the new department's id: ")
            specialist.name = name
            specialist.specialty = specialty
            specialist.department_id = department_id
            specialist.update()
            print(f'Success: {specialist} has been updated.')
        except Exception as exc:
            print("Error updating specialist: ", exc)
    else:
        print(f'Specialist {id_} not found')

def delete_specialist():
    id_ = input("Enter the specialist's id: ")
    specialist = Specialist.find_by_id(id_)
    if specialist:
        specialist.delete()
        print(f'Specialist {id_} deleted')
    else:
        print(f'Specialist {id_} not found')

def list_appointment_specialist():
    appointments = Appointment.get_all() 
    for appointment in appointments:
        print(appointment) 


# Patient Functions

def list_patient():
    patients = Patient.get_all()
    for patient in patients:
        print(patient)

def find_patient_by_name():
    name = input("Enter the patient's name: ")
    patient = Patient.find_by_name(name)
    print(patient) if patient else print(f'Patient {name} not found')

def find_patient_by_id():
    id_ = input("Enter the patient's id: ")
    patient = Patient.find_by_id(id_)
    print(patient) if patient else print(f'Patient {id_} not found')

def create_patient():
    name = input("Enter the patient's name: ")
    age = input("Enter the patient's age: ")
    sex = input("Enter the patient's sex: ")
    
    try:
        age = int(age)
        if age < 0:
            raise ValueError("Age must be a non-negative integer.")
        
        # Create a new patient instance
        patient = Patient(name=name, age=age, sex=sex)

        # Add to session and commit
        session.add(patient)
        session.commit()
        print(f'Success: Patient {patient.name} was created.')
    except ValueError as ve:
        print("Error: ", ve)
    except Exception as exc:
        session.rollback()  # Roll back in case of an error
        print("Error creating patient: ", exc)

def update_patient():
    id_ = input("Enter the patient's id: ")
    patient = Patient.find_by_id(id_)
    if patient:
        try:
            name = input("Enter the patient's new name: ")
            age = int(input("Enter the patient's new age: "))
            sex = input("Enter the patient's new sex: ")

            patient.name = name
            patient.age = age
            patient.sex = sex
            patient.update()
            print(f'Success: {patient}')
        except Exception as exc:
            print("Error updating patient: ", exc)
    else:
        print(f'Patient {id_} not found')

def delete_patient():
    id_ = input("Enter the patient's id: ")
    patient = Patient.find_by_id(id_)
    if patient:
        patient.delete()
        print(f'Patient {id_} deleted')
    else:
        print(f'Patient {id_} not found')

def list_appointment_patient():
    appointments = Appointment.get_all() 
    for appointment in appointments:
        print(appointment) 


# Appointment Functions

def list_appointment():
    appointments = Appointment.get_all()
    for appointment in appointments:
        print(appointment)

def find_appointment_by_name():
    name = input("Enter the patient's name: ")
    appointment = Appointment.find_by_patient_name(name)
    print(appointment) if appointment else print(f'No appointments found for patient {name}')

def find_appointment_by_id():
    id_ = input("Enter the appointment id: ")
    appointment = Appointment.find_by_id(id_)
    print(appointment) if appointment else print(f'Appointment {id_} not found')


def find_appointment_by_date():
    date_str = input("Enter the appointment date (YYYY-MM-DD): ")
    try:
        
        date_ = datetime.strptime(date_str, "%Y-%m-%d").date()
        
        
        appointments = Appointment.find_by_date(date_)
        
        if appointments:
            for appointment in appointments:
                print(appointment)
        else:
            print(f'No appointments found for date {date_str}.')
    except ValueError:
        print("Error: Invalid date format. Please use YYYY-MM-DD.")

def find_appointment_by_specialist_name():
    name = input("Enter the specialist's name: ")
    appointments = Appointment.find_by_specialist_name(name)
    
    if appointments:
        for appointment in appointments:
            print(appointment)
    else:
        print(f'No appointments found for {name}.')

def create_appointment():
    try:
        patient_id = input("Enter the patient's id: ")
        specialist_id = input("Enter the specialist's id: ")
        
        # Validate IDs
        if not Patient.find_by_id(patient_id):
            print(f"Error: Patient ID {patient_id} does not exist.")
            return
        if not Specialist.find_by_id(specialist_id):
            print(f"Error: Specialist ID {specialist_id} does not exist.")
            return
        
        appointment_date_str = input("Enter the appointment date and time (YYYY-MM-DD HH:MM): ")
        
        # Parse the appointment time
        try:
            appointment_time = datetime.strptime(appointment_date_str, "%Y-%m-%d %H:%M")
        except ValueError:
            print("Error: Invalid date format. Please use YYYY-MM-DD HH:MM.")
            return
        
        department_id = input("Enter the department's id: ")
        if not Department.find_by_id(department_id):
            print(f"Error: Department ID {department_id} does not exist.")
            return
        
        # Create the appointment
        appointment = Appointment.create(patient_id, specialist_id, appointment_time, department_id)
        print(f'Success: Appointment created for patient ID {patient_id} with specialist ID {specialist_id} on {appointment_time}.')
    
    except Exception as exc:
        print("Error creating appointment: ", exc)


#def create_appointment():
    #patient_id = input("Enter the patient's id: ")
    #specialist_id = input("Enter the specialist's id: ")
    #appointment_date_str= input("Enter the appointment date (YYYY-MM-DD): ")
    # try:
    #     appointment_time = datetime.strptime(appointment_date_str, "%Y-%m-%d %H:%M")
    #     department_id = input("Enter the department's id: ")
        
    #     appointment = Appointment.create(patient_id, specialist_id, appointment_time, department_id)
    #     print(f'Success: {appointment}')

    # except ValueError as ve:
    #     print("Error: Invalid date format.", ve)

    # except Exception as exc:
    #     print("Error creating appointment: ", exc)
    # try:
    #     appointment_time = datetime.strptime(appointment_date_str, "%Y-%m-%d %H:%M")
    #     department_id = input("Enter the department's id: ")
        
    #     # Create the appointment
    #     appointment = Appointment.create(patient_id, specialist_id, appointment_time, department_id)
    #     print(f'Success: {appointment}')

    # except ValueError as ve:
    #     print("Error: Invalid input.", ve)

    # except Exception as exc:
    #     print("Error creating appointment: ", exc)
            
def update_appointment():
    id_ = input("Enter the appointment's id: ")
    appointment = Appointment.find_by_id(id_)
    if appointment:
        try:
            patient_id = input("Enter the new patient's id: ")
            specialist_id = input("Enter the new specialist's id: ")
            appointment_date_str = input("Enter the new appointment date (YYYY-MM-DD): ")
            appointment_time = datetime.strptime(appointment_date_str, "%Y-%m-%d %HH:%M")
            
            appointment.patient_id = patient_id
            appointment.specialist_id = specialist_id
            appointment.appointment_time = appointment_time  
            appointment.update()
            print(f'Success: {appointment}')
        except Exception as exc:
            print("Error updating appointment: ", exc)
    else:
        print(f'Appointment {id_} not found')


def delete_appointment():
    id_ = input("Enter the appointment's id: ")
    appointment = Appointment.find_by_id(id_)
    if appointment:
        appointment.delete()
        print(f'Appointment {id_} deleted')
    else:
        print(f'Appointment {id_} not found')
