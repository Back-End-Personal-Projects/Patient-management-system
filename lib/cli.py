from lib.helpers import (
    exit_program,
    list_departments,
    find_department_by_name,
    find_department_by_id,
    create_department,
    update_department,
    delete_department,
    list_specialist,
    find_specialist_by_name,
    find_specialist_by_id,
    create_specialist,
    update_specialist,
    delete_specialist,
    list_patient,
    find_patient_by_name,
    find_patient_by_id,
    create_patient,
    update_patient,
    delete_patient,
    list_appointment,
    find_appointment_by_name,
    find_appointment_by_specialist_name,
    find_appointment_by_date,
    create_appointment,
    update_appointment,
    delete_appointment
    
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            patient_menu()  
        elif choice == "2":
            specialist_menu()  
        elif choice == "3":
            appointment_menu()  
        elif choice == "4":
            department_menu()  
        else:
            print("Invalid choice, please try again.")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Manage patients")
    print("2. Manage specialists")
    print("3. Manage appointments")
    print("4. Manage departments")

def department_menu():
    while True:

        print("Department Management:")
        print("0. Go back")
        print("1. List all departments")
        print("2. Find department by name")
        print("3. Find department by id")
        print("4. Create department")
        print("5. Update department")
        print("6. Delete department")
        
        choice = input("> ")
        if choice == "0":
            return  
        elif choice == "1":
            list_departments()
        elif choice == "2":
            find_department_by_name()
        elif choice == "3":
            find_department_by_id()
        elif choice == "4":
            create_department()
        elif choice == "5":
            update_department()
        elif choice == "6":
            delete_department()
        else:
            print("Invalid choice, please try again.")     

def patient_menu():
    while True:
        print("\nPatient Management:")
        print("0. Go back")
        print("1. List all patients")
        print("2. Find patient by name")
        print("3. Find patient by id")
        print("4. Create patient")
        print("5. Update patient")
        print("6. Delete patient")
        choice = input("> ")
        if choice == "0":
            break
        elif choice == "1":
            list_patient()
        elif choice == "2":
            find_patient_by_name()
        elif choice == "3":
            find_patient_by_id()
        elif choice == "4":
            create_patient()
        elif choice == "5":
            update_patient()
        elif choice == "6":
            delete_patient()
        else:
            print("Invalid choice, please try again.")


def specialist_menu():
    while True:
        print("\nSpecialist Management:")
        print("0. Go back")
        print("1. List all specialists")
        print("2. Find specialist by name")
        print("3. Find specialist by id")
        print("4. Create specialist")
        print("5. Update specialist")
        print("6. Delete specialist")
        choice = input("> ")
        if choice == "0":
            break
        elif choice == "1":
            list_specialist()
        elif choice == "2":
            find_specialist_by_name()
        elif choice == "3":
            find_specialist_by_id()
        elif choice == "4":
            create_specialist()
        elif choice == "5":
            update_specialist()
        elif choice == "6":
            delete_specialist()
        else:
            print("Invalid choice, please try again.")


def appointment_menu():
    while True:
        print("\nAppointment Management:")
        print("0. Go back")
        print("1. List all appointments")
        print("2. Find appointment by patient name")
        print("3. Find appointment by specialist name")
        print("4. Find appointment by date")
        print("5. Create appointment")
        print("6. Update appointment")
        print("7. Delete appointment")
        
        choice = input("> ")
        if choice == "0":
            break
        elif choice == "1":
            list_appointment()
        elif choice == "2":
            find_appointment_by_name()  
        elif choice == "3":
            find_appointment_by_specialist_name()
        elif choice == "4":
            find_appointment_by_date() 
        elif choice == "5":
            create_appointment()
        elif choice == "6":
            update_appointment()
        elif choice == "7":
            delete_appointment()
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
