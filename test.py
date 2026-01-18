import pandas as pd
from faker import Faker
import random

# Faker configured for Indian data
fake = Faker("en_IN")

TOTAL_RECORDS = 1000

# ================= PATIENT TABLE =================
patients = []
for i in range(1, TOTAL_RECORDS + 1):
    patients.append({
        "PatientID": i,
        "Name": fake.name(),
        "DateOfBirth": fake.date_of_birth(minimum_age=1, maximum_age=90),
        "Gender": random.choice(["Male", "Female", "Other"]),
        "Address": fake.address().replace("\n", ", "),
        "PhoneNumber": fake.phone_number(),
        "Email": fake.email()
    })
patients_df = pd.DataFrame(patients)

# ================= DEPARTMENT TABLE =================
departments = [
    {"DepartmentID": 1, "DepartmentName": "Cardiology", "Location": "Block A"},
    {"DepartmentID": 2, "DepartmentName": "Neurology", "Location": "Block B"},
    {"DepartmentID": 3, "DepartmentName": "Orthopedics", "Location": "Block C"},
    {"DepartmentID": 4, "DepartmentName": "Pediatrics", "Location": "Block D"},
    {"DepartmentID": 5, "DepartmentName": "General Medicine", "Location": "Block E"},
]
departments_df = pd.DataFrame(departments)

# ================= DOCTOR TABLE =================
doctors = []
for i in range(1, TOTAL_RECORDS + 1):
    dept = random.choice(departments)
    doctors.append({
        "DoctorID": i,
        "Name": fake.name(),
        "Specialization": dept["DepartmentName"],
        "PhoneNumber": fake.phone_number(),
        "Email": fake.email(),
        "DepartmentID": dept["DepartmentID"]
    })
doctors_df = pd.DataFrame(doctors)

# ================= APPOINTMENT TABLE =================
appointments = []
for i in range(1, TOTAL_RECORDS + 1):
    appointments.append({
        "AppointmentID": i,
        "PatientID": random.randint(1, TOTAL_RECORDS),
        "DoctorID": random.randint(1, TOTAL_RECORDS),
        "AppointmentDate": fake.date_this_year(),
        "AppointmentTime": fake.time(),
        "Status": random.choice(["Scheduled", "Completed", "Cancelled"])
    })
appointments_df = pd.DataFrame(appointments)

# ================= PRESCRIPTION TABLE =================
prescriptions = []
for i in range(1, TOTAL_RECORDS + 1):
    prescriptions.append({
        "PrescriptionID": i,
        "AppointmentID": random.randint(1, TOTAL_RECORDS),
        "MedicationDetails": random.choice([
            "Paracetamol", "Ibuprofen", "Amoxicillin",
            "Metformin", "Azithromycin"
        ]),
        "Dosage": random.choice(["1-0-1", "1-1-1", "0-1-0"]),
        "Duration": random.choice(["5 days", "7 days", "10 days"])
    })
prescriptions_df = pd.DataFrame(prescriptions)

# ================= BILLING TABLE =================
billing = []
for i in range(1, TOTAL_RECORDS + 1):
    billing.append({
        "BillID": i,
        "PatientID": random.randint(1, TOTAL_RECORDS),
        "Amount": random.randint(300, 20000),
        "BillDate": fake.date_this_year(),
        "PaymentStatus": random.choice(["Paid", "Unpaid", "Pending"])
    })
billing_df = pd.DataFrame(billing)

# ================= WRITE TO EXCEL =================
with pd.ExcelWriter("Hospital_Management_System_Data.xlsx", engine="openpyxl") as writer:
    patients_df.to_excel(writer, sheet_name="Patients", index=False)
    doctors_df.to_excel(writer, sheet_name="Doctors", index=False)
    departments_df.to_excel(writer, sheet_name="Departments", index=False)
    appointments_df.to_excel(writer, sheet_name="Appointments", index=False)
    prescriptions_df.to_excel(writer, sheet_name="Prescriptions", index=False)
    billing_df.to_excel(writer, sheet_name="Billing", index=False)

print("Hospital_Management_System_Data.xlsx created successfully")
