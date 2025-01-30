from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from backend.config import Base

class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer)
    gender = Column(String)
    medical_history = Column(String, nullable=True)
    date_of_birth = Column(Date)

    diagnoses = relationship("Diagnosis", back_populates="patient")
