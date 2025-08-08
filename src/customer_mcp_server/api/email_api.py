from config import API_URL
from api.common import safe_request
from schemas.email_schemas import EmailDetails


async def post_email(data: EmailDetails) -> None:
    url = f"{API_URL}/emails/"
    body = data.model_dump()
    await safe_request("POST", url, json=body)
    