from sqlalchemy import Column, Integer, String, ForeignKey
from backend.config import Base

class MentalHealth(Base):
    __tablename__ = "mental_health"

    id = Column(Integer, primary_key=True, index=True)
    condition = Column(String)
    risk_level = Column(String)
    patient_id = Column(Integer, ForeignKey("patients.id"))

    patient = relationship("Patient")
