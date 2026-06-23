import pandas as pd

patients=[]

def add_patients(name, age, gender, diagnosis, doctor, date):
    patients.append({"name": name,
    "age": age,
    "gender": gender,
    "diagnosis": diagnosis,
    "doctor": doctor,
    "date": date})
    output=f"{name}'s details has been added"
    return output

def view_patients():
    if patients:
        for patient in patients:
            print(f"name:{patient['name']}, age:{patient['age']}, gender:{patient['gender']}, diagnosis:{patient['diagnosis']}, doctor:{patient['doctor']}, date{patient['date']} ")
    else:
            print("no patient found")

def del_patient(name):
    for patient in patients:
        if patient['name']==name:
            patients.remove(patient)
            return f"{name} has been deleted"
    return f"{name} not found"

def update_field(name, field, value):
    for patient in patients:
        if patient ['name']==name:
            patient[field]=value
            return f"{field} clear for {name}"
    return f"{name} not found"

def del_field(name, field):
    for patient in patients:
        if patient ['name']==name:
            patient[field]=None
            return f"{field} clear for {name}"
    return f"{name} not found"

def total_patients():
    return f"Total Patients: {len(patients)}"


def export_to_excel():
    df = pd.DataFrame(patients)
    df.to_excel("patients.xlsx", index=False)
    return "Data exported to patients.xlsx"

def main():
    while True:
        output= "1. Add Patient\n2. Update Patient\n3. Delete Patient\n4. Delete Specific Patient\n5.View Patients\n6. Total Patients\n7. Export to Excel\n8 exit"
        print (output)
        choice = int(input("Enter your choice: "))
        if choice == 1:
            name = input("Enter Patients name: ")
            age = int(input("Enter Patient's age: "))
            gender = input("Enter Patients gender: ")
            diagnosis = input("Enter Patients diagnosis: ")
            doctor= input("Enter doctor's name: ")
            date = input("Enter date of admission (DD-MM-YYYY): ")
            print(add_patients(name, age, gender, diagnosis, doctor, date))
        elif choice == 2:
            name = input("Enter patient name: ")
            field = input("Enter field to update (age/gender/diagnosis/doctor/date): ")
            value = input("Enter new value: ")
            print(update_field(name, field, value))
        elif choice == 3:
            name = input("Enter expense name: ")
            print(del_patient(name))
        elif choice == 4:
            name = input("Enter expense name: ")
            field= input("Enter field name: ")
            print(del_field(name,field))
        elif choice == 5:
            view_patients()
        elif choice == 6:
            print(total_patients())
        elif choice ==7:
            print(export_to_excel())
        elif choice == 8:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

main()