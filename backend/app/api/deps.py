from typing import Annotated
from fastapi import Depends
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from collections.abc import Generator

def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

DBSession = Annotated[Session, Depends(get_db)]