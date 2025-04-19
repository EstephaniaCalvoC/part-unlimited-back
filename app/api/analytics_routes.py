"""API routes for analytics parts"""

import logging

from fastapi import APIRouter, Depends

from app.analytics.part import get_top_words
from app.db.session import DBClient, get_db
from app.schemas.analytics import RequestWordFrequency, ResponseWordFrequency

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post(
    "/parts/get-top-common-words",
    response_model=list[ResponseWordFrequency],
    summary="Get top common words from parts descriptions",
    description=(
        "This endpoint allows to skip common words like 'to', 'and', 'of' etc."
        "As default, it will return the top 5 words."
    ),
    tags=["Analytics", "Parts"],
)
def get_top_common_words(request: RequestWordFrequency, db: DBClient = Depends(get_db)):
    """Get top common words from parts descriptions

    Args:
        request (RequestWordFrequency): Request with optional limit and skip parameters
        db (DBClient, optional): Database client. Defaults to Depends(get_db).

    Returns:
        list[ResponseWordFrequency]: List of top common words
    """
    return get_top_words(db, request.limit, request.skip)
