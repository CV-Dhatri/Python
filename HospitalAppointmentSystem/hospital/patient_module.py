

from mysql.connector import Error
from hospital.config import get_connection
from hospital.display import print_header, print_table
from hospital.validators import validate_phone, validate_date, validate_gender, validate_blood_group
from hospital.exceptions import PatientNotFoundError, ValidationError

def register_patient():
    print_header("REGISTER NEW PATIENT")
    
    name = input("Enter Patient Full Name: ").strip()
    if not name:
        print("[!] Patient name cannot be empty.")
        return

    while True:
        gender_raw = input("Enter Gender (Male/Female/Other): ").strip()
        try:
            gender = validate_gender(gender_raw)
            break
        except ValidationError as e:
            print(f"[!] {e}")

    while True:
        dob_raw = input("Enter Date of Birth (YYYY-MM-DD): ").strip()
        try:
            dob = validate_date(dob_raw, allow_past=True)
            break
        except ValidationError as e:
            print(f"[!] {e}")

    while True:
        phone_raw = input("Enter 10-digit Phone Number: ").strip()
        try:
            phone = validate_phone(phone_raw)
            break
        except ValidationError as e:
            print(f"[!] {e}")

    address = input("Enter Address: ").strip()

    while True:
        bg_raw = input("Enter Blood Group (e.g. A+, B+, O+): ").strip()
        try:
            blood_group = validate_blood_group(bg_raw)
            break
        except ValidationError as e:
            print(f"[!] {e}")

    conn = get_connection()
    if not conn:
        return

    try:
        cursor = conn.cursor()
        query = """
            INSERT INTO patients (patient_name, gender, dob, phone, address, blood_group, status)
            VALUES (%s, %s, %s, %s, %s, %s, 'ACTIVE')
        """
        cursor.execute(query, (name, gender, dob, phone, address, blood_group))
        conn.commit()
        print(f"\n[OK] Patient registered successfully with Patient ID: {cursor.lastrowid}")
    except Error as e:
        print(f"[Error] Failed to register patient: {e}")
    finally:
        cursor.close()
        conn.close()

def view_all_patients():
    print_header("ACTIVE PATIENTS LIST")
    conn = get_connection()
    if not conn:
        return

    try:
        cursor = conn.cursor()
        query = """
            SELECT patient_id, patient_name, gender, dob, phone, blood_group, status
            FROM patients
            WHERE status = 'ACTIVE'
            ORDER BY patient_id ASC
        """
        cursor.execute(query)
        rows = cursor.fetchall()
        headers = ["Patient ID", "Name", "Gender", "DOB", "Phone", "Blood Group", "Status"]
        print_table(headers, rows)
    except Error as e:
        print(f"[Error] Failed to fetch patients: {e}")
    finally:
        cursor.close()
        conn.close()

def search_patient_by_phone():
    print_header("SEARCH PATIENT BY PHONE")
    phone = input("Enter 10-digit Phone Number: ").strip()

    conn = get_connection()
    if not conn:
        return

    try:
        cursor = conn.cursor()
        query = """
            SELECT patient_id, patient_name, gender, dob, phone, address, blood_group, status
            FROM patients
            WHERE phone = %s AND status = 'ACTIVE'
        """
        cursor.execute(query, (phone,))
        rows = cursor.fetchall()
        headers = ["ID", "Name", "Gender", "DOB", "Phone", "Address", "Blood Group", "Status"]
        print_table(headers, rows)
    except Error as e:
        print(f"[Error] Failed to search patient: {e}")
    finally:
        cursor.close()
        conn.close()

def update_patient_details():
    print_header("UPDATE PATIENT DETAILS")
    try:
        patient_id = int(input("Enter Patient ID to update: ").strip())
    except ValueError:
        print("[!] Patient ID must be a number.")
        return

    conn = get_connection()
    if not conn:
        return

    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM patients WHERE patient_id = %s AND status = 'ACTIVE'", (patient_id,))
        patient = cursor.fetchone()
        if not patient:
            raise PatientNotFoundError(f"Active patient with ID {patient_id} not found.")

        print(f"Updating details for: {patient['patient_name']} (Phone: {patient['phone']}, Address: {patient['address']})")
        new_phone = input("Enter new 10-digit phone (leave blank to keep current): ").strip()
        new_address = input("Enter new address (leave blank to keep current): ").strip()

        updated_phone = validate_phone(new_phone) if new_phone else patient['phone']
        updated_address = new_address if new_address else patient['address']

        cursor.execute(
            "UPDATE patients SET phone = %s, address = %s WHERE patient_id = %s",
            (updated_phone, updated_address, patient_id)
        )
        conn.commit()
        print(f"\n[OK] Patient ID {patient_id} updated successfully.")
    except (PatientNotFoundError, ValidationError) as app_err:
        print(f"[!] {app_err}")
    except Error as e:
        print(f"[Error] Failed to update patient: {e}")
    finally:
        cursor.close()
        conn.close()

def soft_delete_patient():
    print_header("DEACTIVATE PATIENT (SOFT DELETE)")
    try:
        patient_id = int(input("Enter Patient ID to deactivate: ").strip())
    except ValueError:
        print("[!] Patient ID must be a number.")
        return

    conn = get_connection()
    if not conn:
        return

    try:
        cursor = conn.cursor()
        cursor.execute("SELECT patient_name, status FROM patients WHERE patient_id = %s", (patient_id,))
        record = cursor.fetchone()
        if not record:
            raise PatientNotFoundError(f"Patient with ID {patient_id} does not exist.")
        if record[1] == 'INACTIVE':
            print(f"[!] Patient '{record[0]}' is already deactivated.")
            return

        confirm = input(f"Are you sure you want to deactivate '{record[0]}'? (y/N): ").strip().lower()
        if confirm == 'y':
            cursor.execute("UPDATE patients SET status = 'INACTIVE' WHERE patient_id = %s", (patient_id,))
            conn.commit()
            print(f"\n[OK] Patient ID {patient_id} has been deactivated.")
        else:
            print("[*] Operation cancelled.")
    except PatientNotFoundError as e:
        print(f"[!] {e}")
    except Error as e:
        print(f"[Error] Database operation failed: {e}")
    finally:
        cursor.close()
        conn.close()