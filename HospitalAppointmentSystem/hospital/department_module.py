

from mysql.connector import Error
from hospital.config import get_connection
from hospital.display import print_header, print_table
from hospital.exceptions import DepartmentNotFoundError

def add_department():
    print_header("ADD NEW DEPARTMENT")
    
    dept_name = input("Enter Department Name (e.g., Neurology, Pediatrics): ").strip()
    if not dept_name:
        print("[!] Department name cannot be empty.")
        return
        
    description = input("Enter Description (optional): ").strip()

    conn = get_connection()
    if not conn:
        return

    try:
        cursor = conn.cursor()
        query = "INSERT INTO departments (dept_name, description) VALUES (%s, %s)"
        cursor.execute(query, (dept_name, description if description else None))
        conn.commit()
        print(f"\n[OK] Department '{dept_name}' added successfully with ID: {cursor.lastrowid}")
    except Error as e:
        # Error 1062 is MySQL's duplicate entry error code
        if e.errno == 1062:
            print(f"[!] A department named '{dept_name}' already exists.")
        else:
            print(f"[Error] Failed to add department: {e}")
    finally:
        cursor.close()
        conn.close()

def view_departments():
    print_header("HOSPITAL DEPARTMENTS")
    conn = get_connection()
    if not conn:
        return

    try:
        cursor = conn.cursor()
        cursor.execute("SELECT dept_id, dept_name, description FROM departments ORDER BY dept_id ASC")
        rows = cursor.fetchall()
        headers = ["Dept ID", "Department Name", "Description"]
        print_table(headers, rows)
    except Error as e:
        print(f"[Error] Failed to fetch departments: {e}")
    finally:
        cursor.close()
        conn.close()

def update_department():
    print_header("UPDATE DEPARTMENT")
    try:
        dept_id = int(input("Enter Department ID to update: ").strip())
    except ValueError:
        print("[!] Department ID must be a number.")
        return

    conn = get_connection()
    if not conn:
        return

    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM departments WHERE dept_id = %s", (dept_id,))
        dept = cursor.fetchone()
        if not dept:
            raise DepartmentNotFoundError(f"Department with ID {dept_id} not found.")

        print(f"Updating: {dept['dept_name']} (Description: {dept['description']})")
        new_name = input("Enter new name (leave blank to keep current): ").strip()
        new_desc = input("Enter new description (leave blank to keep current): ").strip()

        updated_name = new_name if new_name else dept['dept_name']
        updated_desc = new_desc if new_desc else dept['description']

        cursor.execute(
            "UPDATE departments SET dept_name = %s, description = %s WHERE dept_id = %s",
            (updated_name, updated_desc, dept_id)
        )
        conn.commit()
        print(f"\n[OK] Department ID {dept_id} updated successfully.")
    except DepartmentNotFoundError as app_err:
        print(f"[!] {app_err}")
    except Error as e:
        if e.errno == 1062:
            print("[!] Another department already has that name.")
        else:
            print(f"[Error] Failed to update department: {e}")
    finally:
        cursor.close()
        conn.close()

def view_doctors_in_department():
    print_header("DOCTORS BY DEPARTMENT")
    try:
        dept_id = int(input("Enter Department ID: ").strip())
    except ValueError:
        print("[!] Department ID must be a number.")
        return

    conn = get_connection()
    if not conn:
        return

    try:
        cursor = conn.cursor()
        
        cursor.execute("SELECT dept_name FROM departments WHERE dept_id = %s", (dept_id,))
        dept = cursor.fetchone()
        if not dept:
            raise DepartmentNotFoundError(f"Department with ID {dept_id} not found.")

        query = """
            SELECT doctor_id, doctor_name, phone, consultation_fee, available_slots 
            FROM doctors 
            WHERE dept_id = %s AND status = 'ACTIVE'
        """
        cursor.execute(query, (dept_id,))
        rows = cursor.fetchall()
        
        print(f"\n--- Doctors in {dept[0]} ---")
        headers = ["Doctor ID", "Name", "Phone", "Fee", "Available Slots"]
        print_table(headers, rows)
        
    except DepartmentNotFoundError as app_err:
        print(f"[!] {app_err}")
    except Error as e:
        print(f"[Error] Failed to fetch doctors: {e}")
    finally:
        cursor.close()
        conn.close()