from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

import models
import schemas
from database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="NurseSync API",
    description="API for managing Nurses, Patients, Medications, and Administration Records",
    version="1.0.0"
)

@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Welcome to the NurseSync API! Visit /docs for full API documentation."}

@app.get("/nurses/", response_model=List[schemas.NurseResponse], tags=["Nurses"])
def get_all_nurses(db: Session = Depends(get_db)):
    """Retrieve all nurses."""
    return db.query(models.Nurse).all()

@app.get("/nurses/{nurse_id}", response_model=schemas.NurseResponse, tags=["Nurses"])
def get_nurse_by_id(nurse_id: int, db: Session = Depends(get_db)):
    """Retrieve a single nurse by ID."""
    nurse = db.query(models.Nurse).filter(models.Nurse.id == nurse_id).first()
    if not nurse:
        raise HTTPException(status_code=404, detail="Nurse not found.")
    return nurse



@app.get("/patients/", response_model=List[schemas.PatientResponse], tags=["Patients"])
def get_all_patients(db: Session = Depends(get_db)):
    """Retrieve all patients."""
    return db.query(models.Patient).all()

@app.get("/patients/{patient_id}", response_model=schemas.PatientResponse, tags=["Patients"])
def get_patient_by_id(patient_id: int, db: Session = Depends(get_db)):
    """Retrieve a single patient by ID."""
    patient = db.query(models.Patient).filter(models.Patient.id == patient_id).first()
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found.")
    return patient

@app.get("/medications/", response_model=List[schemas.MedicationResponse], tags=["Medications"])
def get_all_medications(db: Session = Depends(get_db)):
    """Retrieve all medications."""
    return db.query(models.Medication).all()

@app.get("/medications/{medication_id}", response_model=schemas.MedicationResponse, tags=["Medications"])
def get_medication_by_id(medication_id: int, db: Session = Depends(get_db)):
    """Retrieve a single medication by ID."""
    medication = db.query(models.Medication).filter(models.Medication.id == medication_id).first()
    if not medication:
        raise HTTPException(status_code=404, detail="Medication not found.")
    return medication


@app.get("/administrations/", response_model=List[schemas.AdministrationResponse], tags=["Medication Administrations"])
def get_all_administrations(db: Session = Depends(get_db)):
    """Retrieve all medication administration records."""
    return db.query(models.MedicationAdministration).all()

@app.get("/administrations/{admin_id}", response_model=schemas.AdministrationResponse, tags=["Medication Administrations"])
def get_administration_by_id(admin_id: int, db: Session = Depends(get_db)):
    """Retrieve a single medication administration record by ID."""
    admin_record = db.query(models.MedicationAdministration).filter(models.MedicationAdministration.id == admin_id).first()
    if not admin_record:
        raise HTTPException(status_code=404, detail="Administration record not found.")
    return admin_record

@app.post("/administrations/", response_model=schemas.AdministrationResponse, status_code=status.HTTP_201_CREATED, tags=["Medication Administrations"])
def create_administration(admin: schemas.AdministrationCreate, db: Session = Depends(get_db)):
    """Create a new medication administration record."""
    db_admin = models.MedicationAdministration(**admin.model_dump())
    db.add(db_admin)
    db.commit()
    db.refresh(db_admin)
    return db_admin
