from sqlalchemy.orm import Session
from database.models.clinical_trials import ClinicalTrial

def create_trial(db: Session, patient_id: int, trial_name: str, status: str):
    trial = ClinicalTrial(patient_id=patient_id, trial_name=trial_name, status=status)
    db.add(trial)
    db.commit()
    db.refresh(trial)
    return trial

def get_trial(db: Session, trial_id: int):
    return db.query(ClinicalTrial).filter(ClinicalTrial.id == trial_id).first()

def get_trials_by_patient(db: Session, patient_id: int):
    return db.query(ClinicalTrial).filter(ClinicalTrial.patient_id == patient_id).all()

def update_trial(db: Session, trial_id: int, trial_name: str = None, status: str = None):
    trial = db.query(ClinicalTrial).filter(ClinicalTrial.id == trial_id).first()
    if trial:
        if trial_name:
            trial.trial_name = trial_name
        if status:
            trial.status = status
        db.commit()
        db.refresh(trial)
    return trial

def delete_trial(db: Session, trial_id: int):
    trial = db.query(ClinicalTrial).filter(ClinicalTrial.id == trial_id).first()
    if trial:
        db.delete(trial)
        db.commit()
    return trial