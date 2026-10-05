import datetime
import random
import tkinter as tk
from tkinter import messagebox

import mysql.connector


# -----------------------------
# Database Configuration
# -----------------------------
MYSQL_HOST = "localhost"
MYSQL_USER = "root"
MYSQL_PASSWORD = "student"
DATABASE_NAME = "hello"
PATIENT_TABLE = "apt"


def create_database_connection():
    """Connect to MySQL and prepare the project database/table."""
    connection = mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD
    )

    cursor = connection.cursor()
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DATABASE_NAME}")
    cursor.execute(f"USE {DATABASE_NAME}")

    cursor.execute(
        f"""
        CREATE TABLE IF NOT EXISTS {PATIENT_TABLE} (
            idno VARCHAR(12) PRIMARY KEY,
            name CHAR(20),
            age CHAR(3),
            gender CHAR(1),
            phone VARCHAR(10),
            bg VARCHAR(3)
        )
        """
    )
    connection.commit()
    return connection


database = create_database_connection()
database_cursor = database.cursor(buffered=True)


# -----------------------------
# Patient Registration
# -----------------------------
def save_patient():
    """Save a new patient's details to MySQL."""
    patient_id = patient_id_entry.get()
    patient_name = patient_name_entry.get()
    patient_age = patient_age_entry.get()
    patient_gender = patient_gender_entry.get()
    patient_phone = patient_phone_entry.get()
    blood_group = blood_group_entry.get()

    try:
        database_cursor.execute(
            "INSERT INTO apt VALUES (%s, %s, %s, %s, %s, %s)",
            (
                patient_id,
                patient_name,
                patient_age,
                patient_gender,
                patient_phone,
                blood_group,
            ),
        )
        database.commit()
        messagebox.showinfo("Registration", "YOU HAVE BEEN REGISTERED")
    except mysql.connector.Error as error:
        database.rollback()
        messagebox.showerror("Database Error", str(error))


def open_registration_window():
    """Open the patient registration form."""
    global patient_id_entry
    global patient_name_entry
    global patient_age_entry
    global patient_gender_entry
    global patient_phone_entry
    global blood_group_entry

    registration_window = tk.Toplevel(main_window)
    registration_window.title("Patient Registration")
    registration_window.geometry("300x430")
    registration_window.resizable(False, False)

    tk.Label(
        registration_window,
        text="REGISTER YOURSELF",
        font=("Arial", 20, "bold"),
    ).pack(pady=20)

    form = tk.Frame(registration_window)
    form.pack(pady=10)

    fields = [
        ("PATIENT ID", "patient_id"),
        ("NAME", "patient_name"),
        ("AGE", "patient_age"),
        ("GENDER M/F", "patient_gender"),
        ("PHONE", "patient_phone"),
        ("BLOOD GROUP", "blood_group"),
    ]

    entries = {}

    for row, (label_text, field_name) in enumerate(fields):
        tk.Label(form, text=label_text).grid(
            row=row, column=0, padx=10, pady=10, sticky="w"
        )
        entry = tk.Entry(form)
        entry.grid(row=row, column=1, padx=10, pady=10)
        entries[field_name] = entry

    patient_id_entry = entries["patient_id"]
    patient_name_entry = entries["patient_name"]
    patient_age_entry = entries["patient_age"]
    patient_gender_entry = entries["patient_gender"]
    patient_phone_entry = entries["patient_phone"]
    blood_group_entry = entries["blood_group"]

    tk.Button(
        registration_window,
        text="SUBMIT",
        command=save_patient,
        width=12,
    ).pack(pady=15)


# -----------------------------
# Appointment Management
# -----------------------------
DEPARTMENTS = {
    1: {
        "name": "Cardiologist",
        "doctors": [("Dr. Varun", 201), ("Dr. Hrithik", 202)],
        "days": 3,
    },
    2: {
        "name": "Rheumatologist",
        "doctors": [("Dr. Sidharth", 207), ("Dr. Abhishek", 208)],
        "days": 5,
    },
    3: {
        "name": "Psychiatrist",
        "doctors": [("Dr. Salman", 203), ("Dr. Shahrukh", 204)],
        "days": 3,
    },
    4: {
        "name": "Neurologist",
        "doctors": [("Dr. Ajay", 209), ("Dr. Ranveer", 200)],
        "days": 6,
    },
    5: {
        "name": "Otolaryngologist",
        "doctors": [("Dr. Akshay", 205), ("Dr. Amir", 206)],
        "days": 4,
    },
    6: {
        "name": "MI Room",
        "doctors": [
            ("Dr. Irfan", 401),
            ("Dr. John", 402),
            ("Dr. Sanjay", 403),
            ("Dr. Shahid", 404),
        ],
        "days": 1,
    },
}

APPOINTMENT_NUMBERS = (23, 34, 12, 67, 53, 72)


def show_appointment_details(department_number, patient_name):
    """Generate and display appointment details."""
    department = DEPARTMENTS.get(department_number)

    if department is None:
        messagebox.showwarning(
            "Wrong Input",
            "PLEASE ENTER VALID VALUE"
        )
        return

    doctor_name, room_number = random.choice(department["doctors"])
    appointment_number = random.choice(APPOINTMENT_NUMBERS)
    appointment_date = (
        datetime.date.today()
        + datetime.timedelta(days=department["days"])
    )

    details = (
        f"Your appointment is fixed with Dr. {doctor_name.replace('Dr. ', '')}"
        f"\nDepartment:- {department['name']}"
        f"\nRoom no:- {room_number}"
        f"\nPatient:- {patient_name}"
        f"\nDate:- {appointment_date}"
        f"\nAppointment no:- {appointment_number}"
    )

    messagebox.showinfo("APPOINTMENT DETAILS", details)


def load_patient_for_appointment(patient_id):
    """Find a patient and open the department selection screen."""
    database_cursor.execute(
        "SELECT * FROM apt WHERE idno = %s",
        (patient_id,),
    )
    patient_records = database_cursor.fetchall()

    if not patient_records:
        messagebox.showwarning("Error", "NO DATA FOUND!!")
        return

    patient_record = patient_records[0]
    patient_name = patient_record[1]
    patient_age = patient_record[2]
    patient_phone = patient_record[4]
    patient_blood_group = patient_record[5]

    appointment_window = tk.Toplevel(main_window)
    appointment_window.title("Appointment")
    appointment_window.geometry("380x500")
    appointment_window.resizable(False, False)

    tk.Label(
        appointment_window,
        text="APPOINTMENT",
        font=("Arial", 22, "bold"),
    ).pack(pady=15)

    patient_frame = tk.Frame(appointment_window)
    patient_frame.pack(pady=10)

    patient_details = [
        ("WELCOME", patient_name),
        ("AGE", patient_age),
        ("PHONE", patient_phone),
        ("BLOOD GROUP", patient_blood_group),
    ]

    for row, (label_text, value) in enumerate(patient_details):
        tk.Label(
            patient_frame,
            text=f"{label_text}:-",
        ).grid(row=row, column=0, padx=10, pady=5, sticky="w")

        tk.Label(
            patient_frame,
            text=value,
        ).grid(row=row, column=1, padx=10, pady=5, sticky="w")

    tk.Label(
        appointment_window,
        text="DEPARTMENTS",
        font=("Arial", 12, "bold"),
    ).pack(pady=(20, 5))

    for number, department in DEPARTMENTS.items():
        tk.Label(
            appointment_window,
            text=f"{number}. {department['name']}",
        ).pack(anchor="w", padx=70)

    department_entry = tk.Entry(appointment_window)
    department_entry.pack(pady=10)

    def submit_department():
        try:
            department_number = int(department_entry.get())
            show_appointment_details(department_number, patient_name)
        except ValueError:
            messagebox.showwarning(
                "Wrong Input",
                "PLEASE ENTER A VALID DEPARTMENT NUMBER"
            )

    tk.Button(
        appointment_window,
        text="SUBMIT",
        command=submit_department,
        width=12,
    ).pack(pady=10)


def open_appointment_window():
    """Open the appointment search form."""
    appointment_search = tk.Toplevel(main_window)
    appointment_search.title("Appointment")
    appointment_search.geometry("300x250")
    appointment_search.resizable(False, False)

    tk.Label(
        appointment_search,
        text="APPOINTMENT",
        font=("Arial", 22, "bold"),
    ).pack(pady=25)

    tk.Label(
        appointment_search,
        text="PATIENT ID",
    ).pack(pady=5)

    patient_id_input = tk.Entry(appointment_search)
    patient_id_input.pack()

    tk.Button(
        appointment_search,
        text="SUBMIT",
        command=lambda: load_patient_for_appointment(
            patient_id_input.get()
        ),
        width=12,
    ).pack(pady=15)


# -----------------------------
# Doctor List
# -----------------------------
DOCTORS = [
    ("Dr. Varun", "Cardiologist", 201),
    ("Dr. Hrithik", "Cardiologist", 202),
    ("Dr. Salman", "Psychiatrist", 203),
    ("Dr. Shahrukh", "Psychiatrist", 204),
    ("Dr. Akshay", "Otolaryngologist", 205),
    ("Dr. Amir", "Otolaryngologist", 206),
    ("Dr. Sidharth", "Rheumatologist", 207),
    ("Dr. Abhishek", "Rheumatologist", 208),
    ("Dr. Ajay", "Neurologist", 209),
    ("Dr. Ranveer", "Neurologist", 200),
    ("Dr. Irfan", "MI Room", 401),
    ("Dr. John", "MI Room", 402),
    ("Dr. Sanjay", "MI Room", 403),
    ("Dr. Shahid", "MI Room", 404),
]


def open_doctor_list():
    """Display the hospital's doctor list."""
    doctor_window = tk.Toplevel(main_window)
    doctor_window.title("List of Doctors")
    doctor_window.geometry("600x500")
    doctor_window.resizable(False, False)

    tk.Label(
        doctor_window,
        text="LIST OF DOCTORS",
        font=("Arial", 20, "bold"),
    ).pack(pady=15)

    table = tk.Frame(doctor_window)
    table.pack(pady=10)

    headers = ("NAME OF DOCTOR", "DEPARTMENT", "ROOM NO.")
    for column, header in enumerate(headers):
        tk.Label(
            table,
            text=header,
            font=("Arial", 10, "bold"),
            width=22,
        ).grid(row=0, column=column, padx=5, pady=5)

    for row, doctor in enumerate(DOCTORS, start=1):
        for column, value in enumerate(doctor):
            tk.Label(
                table,
                text=value,
                width=22,
            ).grid(row=row, column=column, padx=5, pady=3)


# -----------------------------
# Hospital Services
# -----------------------------
HOSPITAL_SERVICES = [
    ("X-Ray", 101),
    ("MRI", 102),
    ("CT Scan", 103),
    ("Endoscopy", 104),
    ("Dialysis", 105),
    ("Ultrasound", 301),
    ("EEG", 302),
    ("ENMG", 303),
    ("ECG", 304),
]


def open_services_window():
    """Display available hospital services."""
    services_window = tk.Toplevel(main_window)
    services_window.title("Services Available")
    services_window.geometry("500x450")
    services_window.resizable(False, False)

    tk.Label(
        services_window,
        text="SERVICES AVAILABLE",
        font=("Arial", 20, "bold"),
    ).pack(pady=15)

    service_table = tk.Frame(services_window)
    service_table.pack(pady=10)

    tk.Label(
        service_table,
        text="SERVICE",
        font=("Arial", 10, "bold"),
        width=25,
    ).grid(row=0, column=0, padx=5, pady=5)

    tk.Label(
        service_table,
        text="ROOM NO.",
        font=("Arial", 10, "bold"),
        width=15,
    ).grid(row=0, column=1, padx=5, pady=5)

    for row, (service_name, room_number) in enumerate(
        HOSPITAL_SERVICES, start=1
    ):
        tk.Label(
            service_table,
            text=service_name,
            width=25,
        ).grid(row=row, column=0, padx=5, pady=3)

        tk.Label(
            service_table,
            text=room_number,
            width=15,
        ).grid(row=row, column=1, padx=5, pady=3)

    tk.Label(
        services_window,
        text="For more information, contact the hospital.",
    ).pack(pady=20)


# -----------------------------
# Patient Data Lookup / Modification Interface
# -----------------------------
def find_patient(patient_id):
    """Return patient records matching the supplied ID."""
    database_cursor.execute(
        "SELECT * FROM apt WHERE idno = %s",
        (patient_id,),
    )
    return database_cursor.fetchall()


def open_modification_details(patient_id):
    """Display existing patient details and modification controls."""
    records = find_patient(patient_id)

    if not records:
        messagebox.showwarning("Error", "NO DATA FOUND!!")
        return

    patient_record = records[0]

    modification_window = tk.Toplevel(main_window)
    modification_window.title("Data Modification")
    modification_window.geometry("500x500")
    modification_window.resizable(False, False)

    tk.Label(
        modification_window,
        text="DATA MODIFICATION",
        font=("Arial", 18, "bold"),
    ).pack(pady=15)

    details_frame = tk.Frame(modification_window)
    details_frame.pack(pady=10)

    details = [
        ("NAME", patient_record[1]),
        ("AGE", patient_record[2]),
        ("GENDER", patient_record[3]),
        ("PHONE", patient_record[4]),
        ("BLOOD GROUP", patient_record[5]),
    ]

    for row, (label_text, value) in enumerate(details):
        tk.Label(
            details_frame,
            text=f"{label_text}:-",
        ).grid(row=row, column=0, padx=10, pady=5, sticky="w")

        tk.Label(
            details_frame,
            text=value,
        ).grid(row=row, column=1, padx=10, pady=5, sticky="w")

    tk.Label(
        modification_window,
        text="Modification interface",
        font=("Arial", 11, "bold"),
    ).pack(pady=(15, 5))

    tk.Label(
        modification_window,
        text="The current project displays the existing data and "
             "provides fields for modification.",
    ).pack(pady=5)

    tk.Label(
        modification_window,
        text="Select field number (1-5):",
    ).pack(pady=(15, 5))

    field_choice = tk.Entry(modification_window)
    field_choice.pack()

    tk.Label(
        modification_window,
        text="Enter new value:",
    ).pack(pady=(10, 5))

    new_value = tk.Entry(modification_window)
    new_value.pack()

    def update_patient_data():
        field_map = {
            "1": "name",
            "2": "age",
            "3": "gender",
            "4": "phone",
            "5": "bg",
        }

        selected_field = field_choice.get().strip()
        updated_value = new_value.get().strip()

        if selected_field not in field_map:
            messagebox.showwarning(
                "Invalid Input",
                "Please select a field number from 1 to 5."
            )
            return

        if not updated_value:
            messagebox.showwarning(
                "Invalid Input",
                "Please enter a new value."
            )
            return

        column_name = field_map[selected_field]

        try:
            database_cursor.execute(
                f"UPDATE apt SET {column_name} = %s WHERE idno = %s",
                (updated_value, patient_id),
            )
            database.commit()
            messagebox.showinfo(
                "Success",
                "PATIENT DATA UPDATED SUCCESSFULLY"
            )
            modification_window.destroy()
        except mysql.connector.Error as error:
            database.rollback()
            messagebox.showerror("Database Error", str(error))

    tk.Button(
        modification_window,
        text="UPDATE",
        command=update_patient_data,
        width=12,
    ).pack(pady=15)


def open_modification_search():
    """Open the patient ID search form for data modification."""
    search_window = tk.Toplevel(main_window)
    search_window.title("Modification")
    search_window.geometry("300x250")
    search_window.resizable(False, False)

    tk.Label(
        search_window,
        text="MODIFICATION",
        font=("Arial", 22, "bold"),
    ).pack(pady=25)

    tk.Label(
        search_window,
        text="PATIENT ID",
    ).pack(pady=5)

    patient_id_input = tk.Entry(search_window)
    patient_id_input.pack()

    tk.Button(
        search_window,
        text="SUBMIT",
        command=lambda: open_modification_details(
            patient_id_input.get()
        ),
        width=12,
    ).pack(pady=15)


# -----------------------------
# Main Application
# -----------------------------
def close_application():
    """Close the application and database connection."""
    try:
        database.close()
    finally:
        main_window.destroy()


main_window = tk.Tk()
main_window.title("City Hospital")
main_window.geometry("900x250")
main_window.resizable(False, False)

title_label = tk.Label(
    main_window,
    text="CITY HOSPITAL",
    font=("Arial", 36, "bold"),
    bg="blue",
    fg="white",
    padx=20,
    pady=10,
)
title_label.pack(fill="x")

button_frame = tk.Frame(main_window)
button_frame.pack(pady=35)

tk.Button(
    button_frame,
    text="Registration",
    font=("Arial", 12, "bold"),
    bg="cyan",
    width=15,
    command=open_registration_window,
).grid(row=0, column=0, padx=5)

tk.Button(
    button_frame,
    text="Appointment",
    font=("Arial", 12, "bold"),
    bg="cyan",
    width=15,
    command=open_appointment_window,
).grid(row=0, column=1, padx=5)

tk.Button(
    button_frame,
    text="List of Doctors",
    font=("Arial", 12, "bold"),
    bg="cyan",
    width=15,
    command=open_doctor_list,
).grid(row=0, column=2, padx=5)

tk.Button(
    button_frame,
    text="Services Available",
    font=("Arial", 12, "bold"),
    bg="cyan",
    width=15,
    command=open_services_window,
).grid(row=0, column=3, padx=5)

tk.Button(
    button_frame,
    text="Modify Data",
    font=("Arial", 12, "bold"),
    bg="cyan",
    width=15,
    command=open_modification_search,
).grid(row=0, column=4, padx=5)

tk.Button(
    button_frame,
    text="Exit",
    font=("Arial", 12, "bold"),
    bg="yellow",
    width=15,
    command=close_application,
).grid(row=1, column=2, padx=5, pady=20)

main_window.protocol("WM_DELETE_WINDOW", close_application)
main_window.mainloop()
