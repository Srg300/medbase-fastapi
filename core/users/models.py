from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    is_staff = Column(Boolean, default=False)
    is_superuser = Column(Boolean, default=False)

    __mapper_args__ = {
        'polymorphic_identity': 'users',
    }


class Patient(User):
    __tablename__ = 'patients'

    id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    patient_name = Column(String(50), index=True)
    patient_address = Column(String(250), index=True)
    patient_phone = Column(String(50), index=True)
    doctor_id = Column(Integer, ForeignKey('doctors.id'))
    doctor = relationship('Doctor', backref='patients', foreign_keys=[doctor_id])

    __mapper_args__ = {
        'polymorphic_identity': 'patients',
    }


class Doctor(User):
    __tablename__ = 'doctors'

    id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    doctor_name = Column(String(50), index=True)
    doctor_address = Column(String(250), index=True)
    doctor_phone = Column(String(50), index=True)
    specialization_id = Column(Integer, ForeignKey('specializations.id'))
    specialization = relationship('Specialization', backref='doctors')

    __mapper_args__ = {
        'polymorphic_identity': 'doctors',
    }


class Specialization(Base):
    __tablename__ = 'specializations'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, index=True)

    __mapper_args__ = {
        'polymorphic_identity': 'specializations',
    }
