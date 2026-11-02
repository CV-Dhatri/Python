

from mysql.connector import Error
from hospital.config import get_connection
from hospital.display import print_header, print_table
from hospital.validators import validate_date
from hospital.exceptions import AppointmentNotFoundError, PatientNotFoundError, DoctorNotFoundError, ValidationError

def book_appointment():
    print_header("BOOK NEW APPOINTMENT")
    
    try:
        patient_id = int(input("Enter Patient ID: ").strip())
        doctor_id = int(input("Enter Doctor ID: ").strip())
    except ValueError:
        print("[!] IDs must be numeric.")
        return

    while True:
        date_raw = input("Enter Appointment Date (YYYY-MM-DD): ").strip()
        try:
            appt_date = validate_date(date_raw, allow_past=False)
            break
        except ValidationError as e:
            print(f"[!] {e}")

    time_slot = input("Enter Time Slot (e.g., 10:00-10:30): ").strip()
    notes = input("Enter Notes/Reason (optional): ").strip()

    conn = get_connection()
    if not conn:
        return

    try:
        conn.start_transaction()
        cursor = conn.cursor()
        
        cursor.execute("SELECT status FROM patients WHERE patient_id = %s", (patient_id,))
        p_row = cursor.fetchone()
        if not p_row or p_row[0] != 'ACTIVE':
            raise PatientNotFoundError("Patient is not registered or is inactive.")
            
        cursor.execute("SELECT status FROM doctors WHERE doctor_id = %s", (doctor_id,))
        d_row = cursor.fetchone()
        if not d_row or d_row[0] != 'ACTIVE':
            raise DoctorNotFoundError("Doctor is not registered or is inactive.")

        query = """
            INSERT INTO appointments (patient_id, doctor_id, appointment_date, time_slot, status, notes)
            VALUES (%s, %s, %s, %s, 'BOOKED', %s)
        """
        cursor.execute(query, (patient_id, doctor_id, appt_date, time_slot, notes if notes else None))
        conn.commit()
        
        print(f"\n[OK] Appointment booked successfully! Booking ID: {cursor.lastrowid}")
        
    except PatientNotFoundError as e:
        print(f"[!] {e}")
        conn.rollback()
    except DoctorNotFoundError as e:
        print(f"[!] {e}")
        conn.rollback()
    except Error as e:
        conn.rollback()
        if e.errno == 1062:
            print(f"\n[!] Slot Unavailable: The doctor already has an appointment on {appt_date} at {time_slot}.")
        else:
            print(f"[Error] Failed to book appointment: {e}")
    finally:
        cursor.close()
        conn.close()

def view_appointments_by_date():
    print_header("VIEW APPOINTMENTS BY DATE")
    while True:
        date_raw = input("Enter Date (YYYY-MM-DD): ").strip()
        try:
            target_date = validate_date(date_raw, allow_past=True)
            break
        except ValidationError as e:
            print(f"[!] {e}")

    conn = get_connection()
    if not conn:
        return

    try:
        cursor = conn.cursor()
        query = """
            SELECT a.appointment_id, p.patient_name, d.doctor_name, a.time_slot, a.status 
            FROM appointments a
            JOIN patients p ON a.patient_id = p.patient_id
            JOIN doctors d ON a.doctor_id = d.doctor_id
            WHERE a.appointment_date = %s
            ORDER BY a.time_slot ASC
        """
        cursor.execute(query, (target_date,))
        rows = cursor.fetchall()
        headers = ["Appt ID", "Patient Name", "Doctor Name", "Time Slot", "Status"]
        print(f"\n--- Appointments on {target_date} ---")
        print_table(headers, rows)
    except Error as e:
        print(f"[Error] Database error: {e}")
    finally:
        cursor.close()
        conn.close()

def change_appointment_status(new_status: str):
    action = "CANCEL" if new_status == "CANCELLED" else "COMPLETE"
    print_header(f"{action} APPOINTMENT")
    
    try:
        appt_id = int(input("Enter Appointment ID: ").strip())
    except ValueError:
        print("[!] Appointment ID must be a number.")
        return

    conn = get_connection()
    if not conn:
        return

    try:
        cursor = conn.cursor()
        cursor.execute("SELECT status FROM appointments WHERE appointment_id = %s", (appt_id,))
        row = cursor.fetchone()
        
        if not row:
            raise AppointmentNotFoundError(f"Appointment ID {appt_id} not found.")
        
        current_status = row[0]
        if current_status == new_status:
            print(f"[!] Appointment is already marked as {new_status}.")
            return
        if current_status == 'CANCELLED' or current_status == 'COMPLETED':
            print(f"[!] Cannot modify an appointment that is already {current_status}.")
            return

        cursor.execute("UPDATE appointments SET status = %s WHERE appointment_id = %s", (new_status, appt_id))
        conn.commit()
        print(f"\n[OK] Appointment ID {appt_id} successfully marked as {new_status}.")
        
    except AppointmentNotFoundError as e:
        print(f"[!] {e}")
    except Error as e:
        print(f"[Error] Failed to update status: {e}")
    finally:
        cursor.close()
        conn.close()

def cancel_appointment():
    change_appointment_status("CANCELLED")

def mark_appointment_completed():
    change_appointment_status("COMPLETED")