from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from typing_extensions import Annotated
from sqlalchemy.orm import Session
from fastapi import Depends
import os

# Use environment variable for database URL, fallback to local development
DATABASE_URL = os.getenv(
    "DATABASE_URL", 
    "mysql+pymysql://sql12796854:n433v3Vgav@sql12.freesqldatabase.com/sql12796854"
)

# Handle Railway's MySQL URL format
if DATABASE_URL.startswith("mysql://"):
    DATABASE_URL = DATABASE_URL.replace("mysql://", "mysql+pymysql://", 1)

engine = create_engine(DATABASE_URL, echo=True)

# SessionLocal class will be used to create DB sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]