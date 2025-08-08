from typing import Union

from mcp.types import CallToolResult, TextContent
from modular_mcp.bundle import Bundle

from schemas.review_schemas import ReviewSentiment, Review
from exceptions import MemCommerceAPIException
from api.review_api import patch_review_sentiment


bundle = Bundle()


@bundle.tool()
async def add_review_sentiment(review_id: str, review_sentiment: ReviewSentiment) -> Union[Review, CallToolResult]:
    try:
        review = await patch_review_sentiment(review_id, review_sentiment)
    except MemCommerceAPIException as e:
        return CallToolResult(
            isError=True,
            content=[TextContent(type="text", text=f"MemCommerce API Error: {e}")],
        )

    return review
