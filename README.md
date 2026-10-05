# 🏥 Hospital Management System

A simple **Hospital Management System** developed using **Python, Tkinter, and MySQL**.  
The application provides a graphical interface for patient registration, appointment management, doctor information, hospital services, and patient data modification.

---

## 📌 Project Overview

The Hospital Management System is a desktop-based application designed to simplify basic hospital management operations.

The application uses:

- **Python** for programming
- **Tkinter** for the graphical user interface
- **MySQL** for database management
- **MySQL Connector/Python** for connecting Python with MySQL

---

## ✨ Features

### 👤 Patient Registration
- Register new patients
- Store patient information in the MySQL database
- Patient details include:
  - Patient ID
  - Name
  - Age
  - Gender
  - Phone Number
  - Blood Group

### 📅 Appointment Management
- Search for a registered patient
- Select a hospital department
- Assign a doctor
- Generate an appointment date
- Generate an appointment number

### 👨‍⚕️ Doctor Information
Displays:
- Doctor names
- Departments
- Room numbers

### 🏥 Hospital Services
Displays available hospital services such as:

- X-Ray
- MRI
- CT Scan
- Endoscopy
- Dialysis
- Ultrasound
- EEG
- ENMG
- ECG

### ✏️ Patient Data Modification
Provides an interface for modifying registered patient information.

### 🗄️ MySQL Database
The application connects to a local MySQL server and automatically creates the required database and patient table.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Application development |
| Tkinter | Graphical User Interface |
| MySQL | Database management |
| MySQL Connector/Python | Python-MySQL connectivity |

---

## 📋 Requirements

Before running the project, make sure you have:

- Python 3.x
- MySQL Server
- MySQL Connector/Python

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/Hospital-Management-System.git
```

Move into the project directory:

```bash
cd Hospital-Management-System
```

### 2. Install Required Python Package

Run:

```bash
pip install -r requirements.txt
```

Or install the MySQL connector directly:

```bash
pip install mysql-connector-python
```

### 3. Start MySQL

Make sure your local MySQL server is running before launching the application.

---

## 🔐 MySQL Configuration

The application currently connects to MySQL using:

```python
con=sqltor.connect(
    host="localhost",
    user="root",
    password="student"
)
```

Make sure these credentials match your local MySQL configuration.

> **Note:** The password shown above is intended for the local/academic setup of this project. For production applications, database credentials should be stored securely using environment variables or a secrets manager.

---

## ▶️ Running the Application

Run the main Python file:

```bash
python hospital_management.py
```

If your main file has a different name, use that filename instead.

---

## 🗃️ Database

The application automatically creates a database named:

```text
hello
```

It also creates the required patient table:

```text
apt
```

The patient table stores:

| Field | Description |
|-------|-------------|
| `idno` | Patient ID |
| `name` | Patient Name |
| `age` | Patient Age |
| `gender` | Patient Gender |
| `phone` | Patient Phone Number |
| `bg` | Blood Group |

---

## 📂 Project Structure

```text
Hospital-Management-System/
│
├── hospital_management.py
├── importingmodule.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🖥️ Application Modules

The main application provides the following options:

```text
1. Registration
2. Appointment
3. List of Doctors
4. Services Available
5. Modify Data
6. Exit
```

---

## 🔄 Application Flow

```text
Start Application
       │
       ▼
   Main Menu
       │
       ├── Patient Registration
       │        │
       │        ▼
       │    MySQL Database
       │
       ├── Appointment
       │        │
       │        ▼
       │    Doctor / Department
       │
       ├── List of Doctors
       │
       ├── Services Available
       │
       ├── Modify Patient Data
       │
       └── Exit
```

---

## 🎯 Project Objectives

The main objectives of this project are:

- To develop a basic hospital management application.
- To implement a graphical user interface using Tkinter.
- To connect a Python application with a MySQL database.
- To store and retrieve patient information.
- To provide basic appointment management functionality.
- To understand database connectivity in Python.

---

## 👨‍💻 Author

**Preetkumar Kayasth**

---

## 📚 Project Type

**Academic / Educational Project**

Developed for learning and demonstrating concepts related to:

- Python Programming
- GUI Development
- Database Management
- MySQL
- Python-MySQL Connectivity

---

## ⭐ Future Improvements

Possible future improvements include:

- Secure user authentication
- Admin and doctor login
- Better appointment scheduling
- Patient medical history
- Billing and payment management
- Prescription management
- Improved database design
- Input validation
- Password encryption
- Modern GUI design

---

## 📄 License

This project is intended primarily for educational and academic purposes.
```

```bash
git clone https://github.com/YOUR-USERNAME/Hospital-Management-System.git
```

you can replace `YOUR-USERNAME` with your actual GitHub username later. **You don't need to change it right now** if you're just uploading the README.

Your actual source code confirms that the application uses Tkinter, `mysql.connector`, and creates/uses the `hello` database and `apt` patient table, so the README above reflects the project you actually uploaded rather than describing a different system. tkinter city hospital
