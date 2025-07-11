import uuid
from sqlalchemy import Column, String, Integer
from sqlalchemy.dialects.postgresql import UUID
from database import Base

class ParsonsProblem(Base):
    __tablename__ = "parsons_problem"

    #uuid v4 primary key
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, index=True)
    #name
    name = Column(String, index=True)
    #description of the problem
    description = Column(String, index=True)
    #solution code
    solution_code = Column(String, index=True)
    #difficulty level (nullable)
    difficulty = Column(Integer, nullable=True)
    #language of the problem 
    language = Column(String, index=True)