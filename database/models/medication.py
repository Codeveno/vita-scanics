from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from database import Base

class Medication(Base):
    __tablename__ = 'medications'

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey('patients.id'), nullable=False)
    drug_name = Column(String(100), nullable=False)
    dosage = Column(String(50), nullable=False)
    created_at = Column(DateTime, default=func.now())

    patient = relationship("Patient", back_populates="medications")

    def __repr__(self):
        return f'<Medication {self.drug_name}>'