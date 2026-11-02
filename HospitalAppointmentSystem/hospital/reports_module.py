
from mysql.connector import Error
from hospital.config import get_connection
from hospital.display import print_header, print_table

def todays_appointments():
    print_header("TODAY'S APPOINTMENTS")
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
            WHERE a.appointment_date = CURDATE()
            ORDER BY a.time_slot ASC
        """
        cursor.execute(query)
        rows = cursor.fetchall()
        headers = ["Appt ID", "Patient Name", "Doctor Name", "Time Slot", "Status"]
        print_table(headers, rows)
    except Error as e:
        print(f"[Error] Failed to generate report: {e}")
    finally:
        cursor.close()
        conn.close()

def doctor_wise_count():
    print_header("DOCTOR-WISE APPOINTMENT COUNT")
    conn = get_connection()
    if not conn:
        return

    try:
        cursor = conn.cursor()
        query = """
            SELECT d.doctor_name, dep.dept_name, COUNT(a.appointment_id) AS total_appointments
            FROM doctors d
            JOIN departments dep ON d.dept_id = dep.dept_id
            LEFT JOIN appointments a ON d.doctor_id = a.doctor_id
            GROUP BY d.doctor_id, d.doctor_name, dep.dept_name
            ORDER BY total_appointments DESC
        """
        cursor.execute(query)
        rows = cursor.fetchall()
        headers = ["Doctor Name", "Department", "Total Appointments"]
        print_table(headers, rows)
    except Error as e:
        print(f"[Error] Failed to generate report: {e}")
    finally:
        cursor.close()
        conn.close()

def revenue_summary():
    print_header("REVENUE SUMMARY")
    conn = get_connection()
    if not conn:
        return

    try:
        cursor = conn.cursor()
        query = """
            SELECT payment_status, COUNT(bill_id) AS total_bills, SUM(amount) AS total_revenue
            FROM bills
            GROUP BY payment_status
        """
        cursor.execute(query)
        rows = cursor.fetchall()
        headers = ["Payment Status", "Total Bills", "Total Revenue (₹)"]
        print_table(headers, rows)
    except Error as e:
        print(f"[Error] Failed to generate report: {e}")
    finally:
        cursor.close()
        conn.close()