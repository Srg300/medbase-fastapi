from sqlalchemy.orm import Session
from sqlalchemy.sql.functions import mode

from users import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserInDB):
    fake_hashed_password = user.password + "1234"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def create_doctor(db: Session, doctor: schemas.DcotorCreate):
    fake_hashed_password = doctor.password + "1234"
    data = doctor.dict()
    data.pop('password')
    data.update({'hashed_password': fake_hashed_password})
    db_doctor = models.Doctor(**data)
    db.add(db_doctor)
    db.commit()
    db.refresh(db_doctor)
    return db_doctor


def create_patient(db: Session, patient: schemas.PatientCreate):
    fake_hashed_password = patient.password + "1234"
    data = patient.dict()
    data.pop('password')
    data.update({'hashed_password': fake_hashed_password})
    db_patient = models.Patient(**data)
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient


def get_patient(db: Session, patient_id: int):
    return db.query(models.Patient).filter(models.Patient.id == patient_id).first()

    
def get_patients(db: Session,  skip: int = 0, limit: int = 100):
    return db.query(models.Patient).offset(skip).limit(limit).all()


def get_patient_by_email(db: Session, email: str):
    return db.query(models.Patient).filter(models.Patient.email == email).first()


def get_doctor(db: Session, doctor_id: int):
    return db.query(models.Doctor).filter(models.Doctor.id == doctor_id).first()


def get_doctors(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Doctor).offset(skip).limit(limit).all()


def get_doctor_by_email(db: Session, email: str):
    return db.query(models.Doctor).filter(models.Doctor.email == email).first()


def get_specialization(db: Session, specialization_id: int):
    return db.query(models.Specialization).filter(models.Specialization.id == specialization_id).first()


def get_specialization_by_title(db: Session, title: str):
    return db.query(models.Specialization).filter(models.Specialization.title == title).first()


def get_specializations(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Specialization).offset(skip).limit(limit).all()


def create_specialization(db: Session, specialization: schemas.SpecializationCreate):
    db_specialization = models.Specialization(title=specialization.title)
    db.add(db_specialization)
    db.commit()
    db.refresh(db_specialization)
    return db_specialization