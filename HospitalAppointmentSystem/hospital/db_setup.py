import mysql.connector
from mysql.connector import Error
from hospital.config import DB_CONFIG

# DDL for all 5 required tables
TABLE_DEFINITIONS = [
    """
    CREATE TABLE IF NOT EXISTS departments (
        dept_id INT AUTO_INCREMENT PRIMARY KEY,
        dept_name VARCHAR(80) NOT NULL UNIQUE,
        description VARCHAR(255) DEFAULT NULL
    ) ENGINE=InnoDB;
    """,
    """
    CREATE TABLE IF NOT EXISTS doctors (
        doctor_id INT AUTO_INCREMENT PRIMARY KEY,
        doctor_name VARCHAR(100) NOT NULL,
        dept_id INT NOT NULL,
        phone VARCHAR(15),
        consultation_fee DECIMAL(10,2) NOT NULL DEFAULT 500.00,
        available_slots VARCHAR(100) DEFAULT 'Morning,Evening',
        status ENUM('ACTIVE','INACTIVE') DEFAULT 'ACTIVE',
        FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
            ON DELETE RESTRICT ON UPDATE CASCADE
    ) ENGINE=InnoDB;
    """,
    """
    CREATE TABLE IF NOT EXISTS patients (
        patient_id INT AUTO_INCREMENT PRIMARY KEY,
        patient_name VARCHAR(100) NOT NULL,
        gender ENUM('Male','Female','Other'),
        dob DATE,
        phone VARCHAR(15) NOT NULL,
        address VARCHAR(255),
        blood_group VARCHAR(5),
        status ENUM('ACTIVE','INACTIVE') DEFAULT 'ACTIVE',
        registered_at DATETIME DEFAULT CURRENT_TIMESTAMP
    ) ENGINE=InnoDB;
    """,
    """
    CREATE TABLE IF NOT EXISTS appointments (
        appointment_id INT AUTO_INCREMENT PRIMARY KEY,
        patient_id INT NOT NULL,
        doctor_id INT NOT NULL,
        appointment_date DATE NOT NULL,
        time_slot VARCHAR(20) NOT NULL,
        status ENUM('BOOKED','COMPLETED','CANCELLED','NO_SHOW') DEFAULT 'BOOKED',
        notes VARCHAR(255),
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (patient_id) REFERENCES patients(patient_id)
            ON DELETE RESTRICT ON UPDATE CASCADE,
        FOREIGN KEY (doctor_id) REFERENCES doctors(doctor_id)
            ON DELETE RESTRICT ON UPDATE CASCADE,
        UNIQUE KEY uq_doctor_slot (doctor_id, appointment_date, time_slot)
    ) ENGINE=InnoDB;
    """,
    """
    CREATE TABLE IF NOT EXISTS bills (
        bill_id INT AUTO_INCREMENT PRIMARY KEY,
        appointment_id INT NOT NULL UNIQUE,
        amount DECIMAL(10,2) NOT NULL,
        payment_status ENUM('PENDING','PAID') DEFAULT 'PENDING',
        billed_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (appointment_id) REFERENCES appointments(appointment_id)
            ON DELETE RESTRICT ON UPDATE CASCADE
    ) ENGINE=InnoDB;
    """
]

def init_database():
    admin_config = DB_CONFIG.copy()
    db_name = admin_config.pop("database", "hospital_db")

    try:
        conn = mysql.connector.connect(**admin_config)
        cursor = conn.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name};")
        print(f"[OK] Database '{db_name}' verified/created.")
        cursor.close()
        conn.close()
    except Error as e:
        print(f"[Error] Could not initialize database: {e}")
        return

    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()

        for ddl in TABLE_DEFINITIONS:
            cursor.execute(ddl)
        print("[OK] All 5 tables created successfully.")

        cursor.execute("SELECT COUNT(*) FROM departments;")
        if cursor.fetchone()[0] == 0:
            cursor.executemany(
                "INSERT INTO departments (dept_name, description) VALUES (%s, %s);",
                [
                    ("Cardiology", "Heart and cardiovascular care"),
                    ("Orthopedics", "Bones, joints, and spine treatment"),
                    ("General Medicine", "Primary healthcare and diagnostics")
                ]
            )
            cursor.executemany(
                """
                INSERT INTO doctors (doctor_name, dept_id, phone, consultation_fee, available_slots)
                VALUES (%s, %s, %s, %s, %s);
                """,
                [
                    ("Dr. Meridith Grey", 1, "9876543210", 800.00, "10:00-10:30,10:30-11:00"),
                    ("Dr. Richard Webber", 2, "9876543211", 600.00, "11:00-11:30,11:30-12:00"),
                    ("Dr. Derek Shepherd", 3, "9876543212", 500.00, "14:00-14:30,14:30-15:00")
                ]
            )
            conn.commit()
            print("[OK] Seed data inserted successfully.")

        cursor.close()
        conn.close()
        print("[Done] Database setup complete!")
    except Error as e:
        print(f"[Error] Setup execution failed: {e}")

if __name__ == "__main__":
    init_database()