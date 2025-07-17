from config import API_URL
from api.common import safe_request
from schemas.order_schemas import OrderListData, OrderData


async def get_user_orders(user_jwt: str) -> OrderListData:
    url = f"{API_URL}/orders/user-orders"
    headers = {"Authorization": f"Bearer {user_jwt}"}
    orders_data = await safe_request("GET", url, headers=headers)
    order_list_data = OrderListData(data=[OrderData(**order) for order in orders_data])
    return order_list_data
