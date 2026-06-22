
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
        for patient in patients.items():
            print(f"name:{patient['name']}, age:{patient['age']}, gender:{patient['gender']}, diagonsis:{patient['diagonsis']}, doctor:{patient['doctor']}, date{patient['patient']} ")
        else:
            print("no patient found")

def del_patient(name):
    for patient in patients:
        if patient['name']==name:
            patients.remove(patient)
            return f"{name} has been deleted"
    return f"{name} was found"

def del_field(name, field):
    for patient in patients:
        if patient ['name']==name:
            patient[field]==None
            return f"{field} clear for {name}"
    return f"{name} not found"

        