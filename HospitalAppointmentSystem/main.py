
import sys
from hospital.patient_module import register_patient, view_all_patients, search_patient_by_phone, update_patient_details, soft_delete_patient
from hospital.department_module import add_department, view_departments, update_department, view_doctors_in_department
from hospital.doctor_module import add_doctor, view_all_doctors, update_doctor_details, deactivate_doctor
from hospital.appointment_module import book_appointment, view_appointments_by_date, cancel_appointment, mark_appointment_completed
from hospital.billing_module import generate_bill, mark_bill_paid, view_all_bills
from hospital.reports_module import todays_appointments, doctor_wise_count, revenue_summary
from hospital.display import print_header

def get_choice(prompt="Enter your choice: "):
    try:
        return int(input(prompt).strip())
    except ValueError:
        return -1

def patient_menu():
    while True:
        print_header("PATIENT MODULE")
        print("1. Register New Patient")
        print("2. View All Active Patients")
        print("3. Search Patient by Phone")
        print("4. Update Patient Details")
        print("5. Deactivate Patient")
        print("6. Back to Main Menu")
        
        choice = get_choice()
        if choice == 1: register_patient()
        elif choice == 2: view_all_patients()
        elif choice == 3: search_patient_by_phone()
        elif choice == 4: update_patient_details()
        elif choice == 5: soft_delete_patient()
        elif choice == 6: break
        else: print("[!] Invalid choice. Please try again.")

def doctor_menu():
    while True:
        print_header("DOCTOR MODULE")
        print("1. Add New Doctor")
        print("2. View All Active Doctors")
        print("3. Update Doctor Details")
        print("4. Deactivate Doctor")
        print("5. Back to Main Menu")
        
        choice = get_choice()
        if choice == 1: add_doctor()
        elif choice == 2: view_all_doctors()
        elif choice == 3: update_doctor_details()
        elif choice == 4: deactivate_doctor()
        elif choice == 5: break
        else: print("[!] Invalid choice. Please try again.")

def department_menu():
    while True:
        print_header("DEPARTMENT MODULE")
        print("1. Add New Department")
        print("2. View All Departments")
        print("3. Update Department")
        print("4. View Doctors in a Department")
        print("5. Back to Main Menu")
        
        choice = get_choice()
        if choice == 1: add_department()
        elif choice == 2: view_departments()
        elif choice == 3: update_department()
        elif choice == 4: view_doctors_in_department()
        elif choice == 5: break
        else: print("[!] Invalid choice. Please try again.")

def appointment_menu():
    while True:
        print_header("APPOINTMENT MODULE")
        print("1. Book New Appointment")
        print("2. Cancel Appointment")
        print("3. View Appointments by Date")
        print("4. Mark Appointment as Completed")
        print("5. Back to Main Menu")
        
        choice = get_choice()
        if choice == 1: book_appointment()
        elif choice == 2: cancel_appointment()
        elif choice == 3: view_appointments_by_date()
        elif choice == 4: mark_appointment_completed()
        elif choice == 5: break
        else: print("[!] Invalid choice. Please try again.")

def billing_menu():
    while True:
        print_header("BILLING MODULE")
        print("1. Generate Bill for Completed Appointment")
        print("2. Mark Bill as Paid")
        print("3. View All Bills")
        print("4. Back to Main Menu")
        
        choice = get_choice()
        if choice == 1: generate_bill()
        elif choice == 2: mark_bill_paid()
        elif choice == 3: view_all_bills()
        elif choice == 4: break
        else: print("[!] Invalid choice. Please try again.")

def reports_menu():
    while True:
        print_header("REPORTS MODULE")
        print("1. Today's Appointments")
        print("2. Doctor-wise Appointment Count")
        print("3. Revenue Summary")
        print("4. Back to Main Menu")
        
        choice = get_choice()
        if choice == 1: todays_appointments()
        elif choice == 2: doctor_wise_count()
        elif choice == 3: revenue_summary()
        elif choice == 4: break
        else: print("[!] Invalid choice. Please try again.")

def main():
    while True:
        print_header("HOSPITAL APPOINTMENT SYSTEM")
        print("1. Patient Module")
        print("2. Doctor Module")
        print("3. Department Module")
        print("4. Appointment Module")
        print("5. Billing Module")
        print("6. Reports Module")
        print("7. Exit")
        
        choice = get_choice()
        if choice == 1: patient_menu()
        elif choice == 2: doctor_menu()
        elif choice == 3: department_menu()
        elif choice == 4: appointment_menu()
        elif choice == 5: billing_menu()
        elif choice == 6: reports_menu()
        elif choice == 7:
            print("\nExiting system. Goodbye!\n")
            sys.exit(0)
        else:
            print("[!] Invalid choice. Please try again.")

if __name__ == "__main__":
    main()