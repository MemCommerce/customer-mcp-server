from pydantic import BaseModel


class ReviewSentiment(BaseModel):
    sentiment: str
    tags: list[str]
    aspect_sentiment: dict[str, str] | None = None


class Review(BaseModel):
    id: str
    rating: int
    title: str | None = None
    content: str | None = None

    sentiment: str | None = None
    tags: list[str] | None = None
    aspect_sentiment: dict[str, str] | None = None

    product_variant_id: str
    order_item_id: str
    user_id: str
