from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

class NurseBase(BaseModel):
    name: str
    email: str

class NurseCreate(NurseBase):
    pass

class NurseResponse(NurseBase):
    id: int
    class Config:
        from_attributes = True

class PatientBase(BaseModel):
    name: str
    age: Optional[int] = None

class PatientCreate(PatientBase):
    pass

class PatientResponse(PatientBase):
    id: int
    class Config:
        from_attributes = True

class MedicationBase(BaseModel):
    name: str
    dosage: Optional[str] = None

class MedicationCreate(MedicationBase):
    pass

class MedicationResponse(MedicationBase):
    id: int
    class Config:
        from_attributes = True

class AdministrationBase(BaseModel):
    patient_id: int
    nurse_id: int
    medication_id: int
    dose_given: str
    administered_at: datetime

class AdministrationCreate(AdministrationBase):
    pass

class AdministrationResponse(AdministrationBase):
    id: int
    class Config:
        from_attributes = True
