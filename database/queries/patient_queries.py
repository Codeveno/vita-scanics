from sqlalchemy.orm import Session
from database.models.patient import Patient

def create_patient(db: Session, name: str, age: int, gender: str, medical_history: str = None):
    patient = Patient(name=name, age=age, gender=gender, medical_history=medical_history)
    db.add(patient)
    db.commit()
    db.refresh(patient)
    return patient

def get_patient(db: Session, patient_id: int):
    return db.query(Patient).filter(Patient.id == patient_id).first()

def get_all_patients(db: Session):
    return db.query(Patient).all()

def update_patient(db: Session, patient_id: int, name: str = None, age: int = None, gender: str = None, medical_history: str = None):
    patient = db.query(Patient).filter(Patient.id == patient_id).first()
    if patient:
        if name:
            patient.name = name
        if age:
            patient.age = age
        if gender:
            patient.gender = gender
        if medical_history:
            patient.medical_history = medical_history
        db.commit()
        db.refresh(patient)
    return patient

def delete_patient(db: Session, patient_id: int):
    patient = db.query(Patient).filter(Patient.id == patient_id).first()
    if patient:
        db.delete(patient)
        db.commit()
    return patient