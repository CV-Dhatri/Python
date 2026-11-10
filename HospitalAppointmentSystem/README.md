# Hospital Appointment System

A robust, Command-Line Interface (CLI) based Hospital Management System built with Python and MySQL. This project demonstrates strict separation of concerns, modular architecture, and advanced relational database concepts including ACID transactions, referential integrity, and custom constraint handling.

## 🚀 Features

* **Patient Management**: Register, search, update, and securely deactivate (soft delete) patient records.
* **Doctor & Department Management**: Map doctors to specific departments, track consultation fees, and manage daily shift availability.
* **Appointment Booking**: Transaction-based booking system with strict double-booking prevention using composite unique constraints.
* **Smart Billing Module**: Enforces real-world business rules (e.g., bills can only be generated for 'COMPLETED' appointments). Prevents duplicate billing.
* **Analytics & Reports**: Real-time reporting for today's schedule, doctor-wise patient loads, and hospital revenue tracking.

## 🛠️ Technology Stack

* **Language**: Python 3.x
* **Database**: MySQL 5.7+ (InnoDB Engine)
* **Libraries**: `mysql-connector-python`, `python-dotenv`

## 🏗️ Project Architecture

The application is structured as a modular Python package to maintain the DRY (Don't Repeat Yourself) principle and Separation of Concerns:

```text
hospital_project/
│
├── .env                    # Environment variables (DB credentials)
├── main.py                 # Application entry point and main menu routing
│
└── hospital/               # Core application package
    ├── __init__.py
    ├── config.py           # Database connection logic
    ├── db_setup.py         # Automated database and table initialization
    ├── exceptions.py       # Custom exception classes for clean error handling
    ├── validators.py       # Input validation logic (dates, phones, etc.)
    ├── display.py          # UI formatting (tables, headers)
    │
    ├── patient_module.py   # Patient CRUD operations
    ├── doctor_module.py    # Doctor CRUD operations
    ├── department_module.py# Department CRUD operations
    ├── appointment_module.py# Booking and transaction logic
    ├── billing_module.py   # Invoicing and payment tracking
    └── reports_module.py   # SQL aggregations and analytics