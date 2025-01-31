from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from database import Base

class ClinicalTrial(Base):
    __tablename__ = 'clinical_trials'

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey('patients.id'), nullable=False)
    trial_name = Column(String(200), nullable=False)
    status = Column(String(50), nullable=False)
    created_at = Column(DateTime, default=func.now())

    patient = relationship("Patient", back_populates="clinical_trials")

    def __repr__(self):
        return f'<ClinicalTrial {self.trial_name}>'