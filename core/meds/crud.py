from sqlalchemy.orm import Session
from sqlalchemy.sql.functions import mode

from meds import schemas
from meds.models import Pill, Recipe


def get_pills(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Pill).offset(skip).limit(limit).all()


# def create_pill(db: Session, pill: schemas.Pill)