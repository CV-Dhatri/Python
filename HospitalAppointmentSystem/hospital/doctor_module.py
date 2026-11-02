

from mysql.connector import Error
from hospital.config import get_connection
from hospital.display import print_header, print_table
from hospital.validators import validate_phone
from hospital.exceptions import DoctorNotFoundError, DepartmentNotFoundError, ValidationError

def add_doctor():
    print_header("ADD NEW DOCTOR")
    
    name = input("Enter Doctor Full Name: ").strip()
    if not name:
        print("[!] Doctor name cannot be empty.")
        return

    try:
        dept_id = int(input("Enter Department ID: ").strip())
    except ValueError:
        print("[!] Department ID must be a number.")
        return

    while True:
        phone_raw = input("Enter 10-digit Phone Number: ").strip()
        try:
            phone = validate_phone(phone_raw)
            break
        except ValidationError as e:
            print(f"[!] {e}")

    try:
        fee = float(input("Enter Consultation Fee (e.g., 500.00): ").strip())
    except ValueError:
        print("[!] Fee must be a valid number.")
        return

    slots = input("Enter Available Slots (e.g., '10:00-12:00, 14:00-16:00'): ").strip()
    if not slots:
        slots = "Morning, Evening"  
    conn = get_connection()
    if not conn:
        return

    try:
        cursor = conn.cursor()
        cursor.execute("SELECT dept_id FROM departments WHERE dept_id = %s", (dept_id,))
        if not cursor.fetchone():
            raise DepartmentNotFoundError(f"Department ID {dept_id} does not exist.")

        query = """
            INSERT INTO doctors (doctor_name, dept_id, phone, consultation_fee, available_slots, status)
            VALUES (%s, %s, %s, %s, %s, 'ACTIVE')
        """
        cursor.execute(query, (name, dept_id, phone, fee, slots))
        conn.commit()
        print(f"\n[OK] Doctor added successfully with Doctor ID: {cursor.lastrowid}")
    except DepartmentNotFoundError as app_err:
        print(f"[!] {app_err}")
    except Error as e:
        print(f"[Error] Failed to add doctor: {e}")
    finally:
        cursor.close()
        conn.close()

def view_all_doctors():
    print_header("ACTIVE DOCTORS LIST")
    conn = get_connection()
    if not conn:
        return

    try:
        cursor = conn.cursor()
        query = """
            SELECT d.doctor_id, d.doctor_name, dep.dept_name, d.phone, d.consultation_fee, d.available_slots
            FROM doctors d
            JOIN departments dep ON d.dept_id = dep.dept_id
            WHERE d.status = 'ACTIVE'
            ORDER BY d.doctor_id ASC
        """
        cursor.execute(query)
        rows = cursor.fetchall()
        headers = ["Doctor ID", "Name", "Department", "Phone", "Fee", "Slots"]
        print_table(headers, rows)
    except Error as e:
        print(f"[Error] Failed to fetch doctors: {e}")
    finally:
        cursor.close()
        conn.close()

def update_doctor_details():
    print_header("UPDATE DOCTOR DETAILS")
    try:
        doc_id = int(input("Enter Doctor ID to update: ").strip())
    except ValueError:
        print("[!] Doctor ID must be a number.")
        return

    conn = get_connection()
    if not conn:
        return

    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM doctors WHERE doctor_id = %s AND status = 'ACTIVE'", (doc_id,))
        doctor = cursor.fetchone()
        if not doctor:
            raise DoctorNotFoundError(f"Active doctor with ID {doc_id} not found.")

        print(f"Updating: {doctor['doctor_name']} (Phone: {doctor['phone']}, Fee: {doctor['consultation_fee']}, Slots: {doctor['available_slots']})")
        
        new_phone = input("Enter new 10-digit phone (leave blank to keep current): ").strip()
        new_fee_raw = input("Enter new consultation fee (leave blank to keep current): ").strip()
        new_slots = input("Enter new available slots (leave blank to keep current): ").strip()

        updated_phone = validate_phone(new_phone) if new_phone else doctor['phone']
        updated_fee = float(new_fee_raw) if new_fee_raw else doctor['consultation_fee']
        updated_slots = new_slots if new_slots else doctor['available_slots']

        cursor.execute(
            "UPDATE doctors SET phone = %s, consultation_fee = %s, available_slots = %s WHERE doctor_id = %s",
            (updated_phone, updated_fee, updated_slots, doc_id)
        )
        conn.commit()
        print(f"\n[OK] Doctor ID {doc_id} updated successfully.")
    except (DoctorNotFoundError, ValidationError) as app_err:
        print(f"[!] {app_err}")
    except ValueError:
        print("[!] Fee must be a valid number.")
    except Error as e:
        print(f"[Error] Failed to update doctor: {e}")
    finally:
        cursor.close()
        conn.close()

def deactivate_doctor():
    print_header("DEACTIVATE DOCTOR (SOFT DELETE)")
    try:
        doc_id = int(input("Enter Doctor ID to deactivate: ").strip())
    except ValueError:
        print("[!] Doctor ID must be a number.")
        return

    conn = get_connection()
    if not conn:
        return

    try:
        cursor = conn.cursor()
        cursor.execute("SELECT doctor_name, status FROM doctors WHERE doctor_id = %s", (doc_id,))
        record = cursor.fetchone()
        if not record:
            raise DoctorNotFoundError(f"Doctor with ID {doc_id} does not exist.")
        if record[1] == 'INACTIVE':
            print(f"[!] Doctor '{record[0]}' is already deactivated.")
            return

        confirm = input(f"Are you sure you want to deactivate Dr. {record[0]}? (y/N): ").strip().lower()
        if confirm == 'y':
            cursor.execute("UPDATE doctors SET status = 'INACTIVE' WHERE doctor_id = %s", (doc_id,))
            conn.commit()
            print(f"\n[OK] Doctor ID {doc_id} has been deactivated.")
        else:
            print("[*] Operation cancelled.")
    except DoctorNotFoundError as e:
        print(f"[!] {e}")
    except Error as e:
        print(f"[Error] Database operation failed: {e}")
    finally:
        cursor.close()
        conn.close()