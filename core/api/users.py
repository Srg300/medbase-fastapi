from typing import List

from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session

from database import get_db
from users import crud, schemas


router = APIRouter()


@router.get("/users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@router.get("/users//user/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserInDB, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@router.get("/doctors/", response_model=List[schemas.Doctor])
def read_doctors(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    doctors = crud.get_doctors(db, skip=skip, limit=limit)
    return doctors


@router.post("/doctor/", response_model=schemas.Doctor)
def create_doctor(doctor: schemas.DcotorCreate, db: Session = Depends(get_db)):
    db_doctor = crud.get_doctor_by_email(db, email=doctor.email)
    if db_doctor:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_doctor(db=db, doctor=doctor)


@router.get('/specializations/', response_model=List[schemas.Specialization])
def read_specializations(skip: int=0, limit: int=100, db: Session = Depends(get_db)):
    specializations = crud.get_specializations(db, skip=skip, limit=limit)
    return specializations


@router.post('/specialization/', response_model=schemas.Specialization)
def create_specializations(specialization: schemas.SpecializationCreate, db: Session = Depends(get_db)):
    db_specialization = crud.get_specialization_by_title(db, title=specialization.title)
    if db_specialization:
        raise HTTPException(status_code=400, detail='Specialization already exits')
    return crud.create_specialization(db=db, specialization=specialization)


@router.get("/patients/", response_model=List[schemas.Patient])
def read_patients(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    patients = crud.get_patients(db, skip=skip, limit=limit)
    return patients


@router.post('/patient', response_model=schemas.Patient)
def create_patient(patient: schemas.PatientCreate, db: Session = Depends(get_db)):
    db_patient = crud.get_patient_by_email(db, email=patient.email)
    if db_patient:
        raise HTTPException(status_code=400, detail='Patient already exist')
    return crud.create_patient(db=db, patient=patient)
