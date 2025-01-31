from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from database import Base

class MentalHealth(Base):
    __tablename__ = 'mental_health'

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey('patients.id'), nullable=False)
    condition = Column(String(200), nullable=False)
    severity = Column(String(50), nullable=False)
    created_at = Column(DateTime, default=func.now())

    patient = relationship("Patient", back_populates="mental_health_records")

    def __repr__(self):
        return f'<MentalHealth {self.condition}>'