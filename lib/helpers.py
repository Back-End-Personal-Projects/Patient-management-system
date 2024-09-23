from lib.models.department import Department
from lib.models.specialist import Specialist
from lib.models.patient import Patient
from lib.models.appointment import Appointment

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
    location = input("Enter the department's location: ")
    try:
        department = Department.create(name, location)
        print(f'Success: {department}')
    except Exception as exc:
        print("Error creating department:", exc)

def update_department():
    id_ = input("Enter the department's id: ")
    department = Department.find_by_id(id_)
    if department:
        try:
            name = input("Enter the department's new name: ")
            location = input("Enter the department's new location: ")
            department.name = name
            department.location = location
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
    department_id = input("Enter the department's id: ")
    try:
        specialist = Specialist.create(name, department_id)
        print(f'Success: {specialist}')
    except Exception as exc:
        print("Error creating specialist: ", exc)

def update_specialist():
    id_ = input("Enter the specialist's id: ")
    specialist = Specialist.find_by_id(id_)
    if specialist:
        try:
            name = input("Enter the specialist's new name: ")
            department_id = input("Enter the new department's id: ")
            specialist.name = name
            specialist.department_id = department_id
            specialist.update()
            print(f'Success: {specialist}')
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
        patient = Patient.create(name, age, sex)
        print(f'Success: {patient}')
    except ValueError:
        print("Error: Age must be a positive integer")
    except Exception as exc:
        print("Error creating patient: ", exc)

def update_patient():
    id_ = input("Enter the patient's id: ")
    patient = Patient.find_by_id(id_)
    if patient:
        try:
            name = input("Enter the patient's new name: ")
            age = input("Enter the patient's new age: ")
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
    appointment = Appointment.find_by_name(name)
    print(appointment) if appointment else print(f'No appointments found for patient {name}')

def find_appointment_by_id():
    id_ = input("Enter the appointment id: ")
    appointment = Appointment.find_by_id(id_)
    print(appointment) if appointment else print(f'Appointment {id_} not found')

def find_appointment_by_date():
    date_ = input("Enter the appointment date: ")
    appointment = Appointment.find_by_date(date_)
    print(appointment) if appointment else print(f'Appointment {date_} not found')

def find_appointment_by_specialist_name():
    name = input("Enter the specialist's name: ")
    appointment = Appointment.find_by_specialist_name(name)
    print(appointment) if appointment else print(f'No appointments found for specialist {name}')

def create_appointment():
    patient_id = input("Enter the patient's id: ")
    specialist_id = input("Enter the specialist's id: ")
    appointment_date = input("Enter the appointment date (YYYY-MM-DD): ")
    try:
        appointment = Appointment.create(patient_id, specialist_id, appointment_date)
        print(f'Success: {appointment}')
    except Exception as exc:
        print("Error creating appointment: ", exc)

def update_appointment():
    id_ = input("Enter the appointment's id: ")
    appointment = Appointment.find_by_id(id_)
    if appointment:
        try:
            patient_id = input("Enter the new patient's id: ")
            specialist_id = input("Enter the new specialist's id: ")
            appointment_date = input("Enter the new appointment date (YYYY-MM-DD): ")
            appointment.patient_id = patient_id
            appointment.specialist_id = specialist_id
            appointment.appointment_date = appointment_date
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
