from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from backend.config import Base

class Medication(Base):
    __tablename__ = "medications"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    dosage = Column(String)
    patient_id = Column(Integer, ForeignKey("patients.id"))

    patient = relationship("Patient")
