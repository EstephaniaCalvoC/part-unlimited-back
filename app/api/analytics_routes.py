"""API routes for analytics parts"""

import logging

from fastapi import APIRouter, Depends

from app.analytics.part import get_top_words
from app.db.session import DBClient, get_db
from app.schemas.analytics import RequestWordFrequency, ResponseWordFrequency

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post("/part/get-top-common-words", response_model=list[ResponseWordFrequency])
def get_top_common_words(request: RequestWordFrequency, db: DBClient = Depends(get_db)):
    return get_top_words(db, request.limit, request.skip)
