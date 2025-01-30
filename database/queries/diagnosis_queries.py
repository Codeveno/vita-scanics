from sqlalchemy.orm import Session
from database.models import Diagnosis

def get_diagnosis_by_patient_id(db: Session, patient_id: int):
    return db.query(Diagnosis).filter(Diagnosis.patient_id == patient_id).all()

def create_diagnosis(db: Session, diagnosis_data):
    db_diagnosis = Diagnosis(**diagnosis_data)
    db.add(db_diagnosis)
    db.commit()
    db.refresh(db_diagnosis)
    return db_diagnosis
