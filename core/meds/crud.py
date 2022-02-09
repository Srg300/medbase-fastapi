from sqlalchemy.orm import Session
from sqlalchemy.sql.functions import mode

from meds import schemas
from meds.models import Pill, Recipe


def get_pills(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Pill).offset(skip).limit(limit).all()


def create_pill(db: Session, pill: schemas.PillCreate):
    db_pill = Pill(name=pill.name)
    db.add(db_pill)
    db.commit()
    db.refresh(db_pill)
    return db_pill


def get_pill(db: Session, name: str):
    return db.query(Pill).filter(Pill.name==name).first()


def delete_pill(db: Session, name: str):
    db_pill = db.query(Pill).filter(Pill.name==name).first()
    return db.delete
