from fastapi import APIRouter
from app.utilities.logger import logger

router = APIRouter()


@router.get("/search")
async def search():
    logger.info("Search endpoint hit")
    return {"message": "Search endpoint hit"}
