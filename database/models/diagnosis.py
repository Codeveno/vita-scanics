from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from database import Base

class Diagnosis(Base):
    __tablename__ = 'diagnoses'

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey('patients.id'), nullable=False)
    condition = Column(String(200), nullable=False)
    confidence_level = Column(Float, nullable=False)
    created_at = Column(DateTime, default=func.now())

    patient = relationship("Patient", back_populates="diagnoses")

    def __repr__(self):
        return f'<Diagnosis {self.condition}>'