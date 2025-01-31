from sqlalchemy.orm import Session
from database.models.diagnosis import Diagnosis

def create_diagnosis(db: Session, patient_id: int, condition: str, confidence_level: float):
    diagnosis = Diagnosis(patient_id=patient_id, condition=condition, confidence_level=confidence_level)
    db.add(diagnosis)
    db.commit()
    db.refresh(diagnosis)
    return diagnosis

def get_diagnosis(db: Session, diagnosis_id: int):
    return db.query(Diagnosis).filter(Diagnosis.id == diagnosis_id).first()

def get_diagnoses_by_patient(db: Session, patient_id: int):
    return db.query(Diagnosis).filter(Diagnosis.patient_id == patient_id).all()

def update_diagnosis(db: Session, diagnosis_id: int, condition: str = None, confidence_level: float = None):
    diagnosis = db.query(Diagnosis).filter(Diagnosis.id == diagnosis_id).first()
    if diagnosis:
        if condition:
            diagnosis.condition = condition
        if confidence_level:
            diagnosis.confidence_level = confidence_level
        db.commit()
        db.refresh(diagnosis)
    return diagnosis

def delete_diagnosis(db: Session, diagnosis_id: int):
    diagnosis = db.query(Diagnosis).filter(Diagnosis.id == diagnosis_id).first()
    if diagnosis:
        db.delete(diagnosis)
        db.commit()
    return diagnosis