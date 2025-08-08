from config import API_URL
from api.common import safe_request
from schemas.review_schemas import Review, ReviewSentiment


async def patch_review_sentiment(review_id: str, review_sentiment: ReviewSentiment) -> Review:
    url = f"{API_URL}/reviews/{review_id}/sentiment"
    body = review_sentiment.model_dump()
    data = await safe_request("PATCH", url, json=body)
    review = Review(**data)
    return review
