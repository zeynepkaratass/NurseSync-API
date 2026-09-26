from sqlalchemy import Column, Integer, String, Date, DateTime, ForeignKey
from database import Base

class Nurse(Base):
    __tablename__ = "nurses"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True)

class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    age = Column(Integer)

class Medication(Base):
    __tablename__ = "medications"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    dosage = Column(String)

class MedicationAdministration(Base):
    __tablename__ = "medication_administrations"

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id"))
    nurse_id = Column(Integer, ForeignKey("nurses.id"))
    medication_id = Column(Integer, ForeignKey("medications.id"))
    dose_given = Column(String)
    administered_at = Column(DateTime)
    