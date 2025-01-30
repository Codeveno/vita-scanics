from sqlalchemy.orm import Session
from database.models import ClinicalTrial

def get_trials_by_condition(db: Session, condition: str):
    return db.query(ClinicalTrial).filter(ClinicalTrial.condition_treated == condition).all()

def create_clinical_trial(db: Session, trial_data):
    db_trial = ClinicalTrial(**trial_data)
    db.add(db_trial)
    db.commit()
    db.refresh(db_trial)
    return db_trial
