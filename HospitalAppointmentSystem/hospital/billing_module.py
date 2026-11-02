
from mysql.connector import Error
from hospital.config import get_connection
from hospital.display import print_header, print_table
from hospital.exceptions import AppointmentNotFoundError

def generate_bill():
    print_header("GENERATE BILL")
    
    try:
        appt_id = int(input("Enter Appointment ID: ").strip())
    except ValueError:
        print("[!] Appointment ID must be a number.")
        return

    conn = get_connection()
    if not conn:
        return

    try:
        cursor = conn.cursor(dictionary=True)
        
        query = """
            SELECT a.status, d.consultation_fee, p.patient_name
            FROM appointments a
            JOIN doctors d ON a.doctor_id = d.doctor_id
            JOIN patients p ON a.patient_id = p.patient_id
            WHERE a.appointment_id = %s
        """
        cursor.execute(query, (appt_id,))
        record = cursor.fetchone()

        if not record:
            raise AppointmentNotFoundError(f"Appointment ID {appt_id} not found.")

        if record['status'] != 'COMPLETED':
            print(f"[!] Billing is only allowed for COMPLETED appointments. Current status: {record['status']}")
            return

        base_fee = record['consultation_fee']
        patient_name = record['patient_name']

        cursor.execute("SELECT bill_id FROM bills WHERE appointment_id = %s", (appt_id,))
        if cursor.fetchone():
            print(f"[!] A bill has already been generated for Appointment ID {appt_id}.")
            return

        insert_query = "INSERT INTO bills (appointment_id, amount, payment_status) VALUES (%s, %s, 'PENDING')"
        cursor.execute(insert_query, (appt_id, base_fee))
        conn.commit()

        print(f"\n[OK] Bill generated successfully for {patient_name}.")
        print(f"     Bill ID: {cursor.lastrowid} | Amount: ₹{base_fee} | Status: PENDING")

    except AppointmentNotFoundError as e:
        print(f"[!] {e}")
    except Error as e:
        print(f"[Error] Database error: {e}")
    finally:
        cursor.close()
        conn.close()

def mark_bill_paid():
    print_header("PAY BILL")
    try:
        bill_id = int(input("Enter Bill ID to mark as PAID: ").strip())
    except ValueError:
        print("[!] Bill ID must be a number.")
        return

    conn = get_connection()
    if not conn:
        return

    try:
        cursor = conn.cursor()
        cursor.execute("SELECT payment_status FROM bills WHERE bill_id = %s", (bill_id,))
        row = cursor.fetchone()

        if not row:
            print(f"[!] Bill ID {bill_id} not found.")
            return

        if row[0] == 'PAID':
            print("[!] This bill is already paid.")
            return

        cursor.execute("UPDATE bills SET payment_status = 'PAID' WHERE bill_id = %s", (bill_id,))
        conn.commit()
        print(f"\n[OK] Bill ID {bill_id} marked as PAID.")

    except Error as e:
        print(f"[Error] Failed to update bill: {e}")
    finally:
        cursor.close()
        conn.close()

def view_all_bills():
    print_header("ALL BILLS")
    conn = get_connection()
    if not conn:
        return

    try:
        cursor = conn.cursor()
        query = """
            SELECT b.bill_id, b.appointment_id, p.patient_name, b.amount, b.payment_status, b.billed_at
            FROM bills b
            JOIN appointments a ON b.appointment_id = a.appointment_id
            JOIN patients p ON a.patient_id = p.patient_id
            ORDER BY b.bill_id DESC
        """
        cursor.execute(query)
        rows = cursor.fetchall()
        headers = ["Bill ID", "Appt ID", "Patient Name", "Amount", "Status", "Billed At"]
        print_table(headers, rows)
    except Error as e:
        print(f"[Error] Failed to fetch bills: {e}")
    finally:
        cursor.close()
        conn.close()