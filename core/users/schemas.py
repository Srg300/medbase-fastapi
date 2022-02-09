from typing import List, Optional
from pydantic import BaseModel


class UserBase(BaseModel):
    email: str

    class Config:
        orm_mode = True


class BasePatient(UserBase):
    id: int


class UserInDB(UserBase):
    password: str
    is_active: bool
    is_staff: bool
    is_superuser: bool


class User(UserBase):
    id: int
    is_active: bool
    is_staff: bool
    is_superuser: bool

    class Config:
        orm_mode = True


class BaseSpecialization(BaseModel):
    id: int
    title: str

    class Config:
        orm_mode = True


class SpecializationCreate(BaseModel):
    title: str

    class Config:
        orm_mode = True


class DoctorBase(BaseModel):
    id: int

    class Config:
        orm_mode = True


class Doctor(DoctorBase):
    # id: int
    doctor_name: str
    doctor_address: str
    doctor_phone: str
    email: str
    is_staff: bool

    patients: list[BasePatient] = []
    specialization: BaseSpecialization

    class Config:
        orm_mode = True


class Specialization(BaseSpecialization):
    doctors: list[DoctorBase] = []


class DcotorCreate(UserInDB):
    doctor_name: str
    doctor_address: str
    doctor_phone: str
    is_staff: bool = True
    is_superuser: bool = False
    specialization_id: int

    class Config:
        orm_mode = True


class Patient(BaseModel):
    id: int
    patient_name: str
    patient_address: str
    patient_phone: str
    email: str

    doctor_id: int

    class Config:
        orm_mode = True


class PatientCreate(UserInDB):
    is_staff: bool = False
    is_superuser: bool = False
    patient_name: str
    patient_address: str
    patient_phone: str
    doctor_id: int

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None
