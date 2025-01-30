from sqlalchemy import Column, Integer, String, ForeignKey
from backend.config import Base

class ClinicalTrial(Base):
    __tablename__ = "clinical_trials"

    id = Column(Integer, primary_key=True, index=True)
    trial_name = Column(String)
    condition_treated = Column(String)
    patient_id = Column(Integer, ForeignKey("patients.id"))

    patient = relationship("Patient")
