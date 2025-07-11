from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

import models, schemas
from database import SessionLocal, engine
from routers import parsons

# Crea le tabelle nel database
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(parsons.router, prefix="/api/parsons", tags=["Parsons Problems"])