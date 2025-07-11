from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from fastapi import HTTPException
import models, schemas
from database import get_db

router = APIRouter()

@router.post("/", response_model=schemas.ParsonsProblemOut)
def crea_problema(problema: schemas.ParsonsProblemCreate, db: Session = Depends(get_db)):
    db_problem = models.ParsonsProblem(**problema.model_dump())
    db.add(db_problem)
    db.commit()
    db.refresh(db_problem)
    return db_problem

@router.get("/hello", response_model=schemas.ParsonsProblemOut)
def hello_problema(db: Session = Depends(get_db)):
    db_problem = db.query(models.ParsonsProblem).first()
    if db_problem is None:
        raise HTTPException(status_code=404, detail="No problem found")
    return db_problem

# get from the database by uuid field
@router.get("/{uuid}", response_model=schemas.ParsonsProblemOut)
def get_parsons_problem(uuid: str, db: Session = Depends(get_db)):
    db_problem = db.query(models.ParsonsProblem).filter(models.ParsonsProblem.uuid == uuid).first()
    if db_problem is None:
        raise HTTPException(status_code=404, detail="Problem not found")
    return db_problem