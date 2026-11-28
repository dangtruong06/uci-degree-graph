from fastapi import APIRouter, HTTPException
from app.api.deps import DBSession
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import text
import logging

router = APIRouter()
logger = logging.getLogger(__name__)

@router.get("/health")
def health_check():
    return {"status": "ok"}


@router.get("/health/db")
def health_check_db(db: DBSession):
    try:
        db.execute(text("SELECT 1"))
    except SQLAlchemyError:
        logger.exception("Database health check failed")
        raise HTTPException(status_code=503, detail="Database unavailable")
    return {"status": "ok"}