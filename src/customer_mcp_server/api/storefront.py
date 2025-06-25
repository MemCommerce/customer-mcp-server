from config import API_URL
from api.common import safe_request
from schemas.storefront_schemas import StorefrontData


async def get_hole_storefront() -> StorefrontData:
    url = f"{API_URL}/storefront/all"
    data = await safe_request("GET", url)
    storefront_data = StorefrontData(**data)
    return storefront_data
