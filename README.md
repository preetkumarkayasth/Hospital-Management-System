# 🏥 Hospital Management System

A desktop-based **Hospital Management System** developed using **Python, Tkinter, and MySQL**.

The application provides a graphical interface for patient registration, appointment management, doctor information, hospital services, and patient data management.

---

## 📌 Project Overview

The Hospital Management System is designed to provide basic hospital management functionality through a graphical user interface.

The application uses:

- **Python** for application development
- **Tkinter** for the graphical user interface
- **MySQL** for database management
- **MySQL Connector/Python** for connecting Python with MySQL

---

## ✨ Features

### 👤 Patient Registration

The application allows new patients to register their information.

Patient details include:

- Patient ID
- Name
- Age
- Gender
- Phone Number
- Blood Group

The registered information is stored in the MySQL database.

---

### 📅 Appointment Management

The application provides an appointment interface for registered patients.

It allows the user to:

- Search for a registered patient using the Patient ID
- Select a hospital department
- Assign a doctor from the selected department
- Generate an appointment date
- Generate an appointment number

---

### 👨‍⚕️ Doctor Information

The application provides a list of available doctors along with:

- Doctor Name
- Department
- Room Number

---

### 🏥 Hospital Services

The application displays available hospital services, including:

- X-Ray
- MRI
- CT Scan
- Endoscopy
- Dialysis
- Ultrasound
- EEG
- ENMG
- ECG

---

### ✏️ Patient Data Modification

The application provides an interface to search for existing patient information and modify patient details.

---

### 🗄️ MySQL Database

The application connects to a local MySQL server and creates the required database and patient table automatically.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Application Development |
| Tkinter | Graphical User Interface |
| MySQL | Database Management |
| MySQL Connector/Python | Python-MySQL Connectivity |

---

## 📋 Requirements

Before running the project, make sure the following are installed:

- Python 3.x
- MySQL Server
- MySQL Connector/Python

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

Open Command Prompt or Terminal and run:

```bash
git clone https://github.com/preetkumarkayasth/Hospital-Management-System.git


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
