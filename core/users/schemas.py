from typing import List, Optional

from pydantic import BaseModel


class UserBase(BaseModel):
    email: str


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


class Specialization(BaseModel):
    id: int
    title: str

    class Config:
        orm_mode = True


class SpecializationCreate(BaseModel):
    title: str

    class Config:
        orm_mode = True


class Doctor(BaseModel):
    doctor_name:str
    doctor_address: str
    doctor_phone: str
    email: str
    is_staff: bool
    
    specialization: Specialization
    class Config:
        orm_mode = True


class DcotorCreate(UserInDB):
    doctor_name:str
    doctor_address: str
    doctor_phone: str
    is_staff: bool = True
    specialization_id: int

    class Config:
        orm_mode = True


class Patient(BaseModel):
    patient_name: str 
    patient_address: str 
    patient_phone: str
    email: str

    doctor: Doctor
    
    class Config:
        orm_mode = True


class PatientCreate(UserInDB):
    patient_name: str 
    patient_address: str 
    patient_phone: str

    doctor: Doctor

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None
