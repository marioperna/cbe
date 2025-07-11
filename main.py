from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

import models, schemas
from database import SessionLocal, engine
from routers import parsons
from fastapi.middleware.cors import CORSMiddleware

# Crea le tabelle nel database
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Aggiunta del middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origin_regex=r"^(http://localhost(:\d+)?|https://.*\.marioperna\.com)$",
    allow_credentials=True,
    allow_methods=["*"],              # Metodi HTTP permessi (GET, POST, etc.)
    allow_headers=["*"],              # Header permessi
)

app.include_router(parsons.router, prefix="/api/parsons", tags=["Parsons Problems"])