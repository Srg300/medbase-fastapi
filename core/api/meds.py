from typing import List

from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session

from database import get_db
from meds import crud, schemas


router = APIRouter()


@router.post('/pills', response_model=schemas.PillCreate)
def create_pill(pill: schemas.PillCreate, db: Session = Depends(get_db)):
    db_pill = crud.get_pill(db, name=pill.name)
    if db_pill:
        raise HTTPException(status_code=400, detail="Pill already registered")
    return crud.create_pill(db=db, pill=pill)


@router.get('/pills', response_model=List[schemas.Pill])
def get_pills(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    pills = crud.get_pills(db, skip=skip, limit=limit)
    return pills
