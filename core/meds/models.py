from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import backref, relationship

from database import Base

from users.models import Doctor, Patient


class Pill(Base):
    __tablename__ = 'pills'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    is_active = Column(Boolean, default=True)


class Recipe(Base):
    __tablename__ = 'recipes'

    id = Column(Integer, primary_key=True, index=True)
    days = Column(String(250), index=True)
    times = Column(String(100), index=True)

    pill_id = Column(ForeignKey('pills.id'))
    pill = relationship('Pill', backref='recepies')

    patient_id = Column(ForeignKey('pills.id'))
    patient = relationship('Patient', backref='recepies')

    doctor_id = Column(ForeignKey('doctors.id'))
    doctor = relationship('Doctor', backref='recepies')