from typing import Union

from mcp.types import CallToolResult, TextContent
from modular_mcp.bundle import Bundle

from schemas.order_schemas import OrderListData
from exceptions import MemCommerceAPIException
from api.order import get_user_orders


bundle = Bundle()


@bundle.tool()
async def list_user_orders(user_jwt: str) -> Union[OrderListData, CallToolResult]:
    """
    Retrieve a list of all orders placed by the user.

    This function fetches all orders associated with the provided user JWT token.
    It returns a structured list of orders, including details such as order ID,
    status, and associated user information along with their respective order items.

    Args:
        user_jwt (str): JSON Web Token (JWT) of the user for authentication.

    Returns:
        Union[OrderListData, CallToolResult]: An OrderListData object containing:
            - data (list[OrderData]): A list of OrderData objects, where each OrderData contains:
                - order (Order): Order information including:
                    - full_name (str): Customer's full name
                    - email (EmailStr): Customer's email address
                    - address (str): Shipping address
                    - city (str): City for shipping
                    - country (str): Country for shipping
                    - status (str): Current order status
                    - id (str): Unique order identifier
                    - user_id (str): ID of the user who placed the order
                - order_items (list[OrderItem]): List of items in the order, where each OrderItem contains:
                    - name (str): Product name
                    - image_url (str | None): Product image URL (optional)
                    - price (float): Item price
                    - quantity (int): Quantity ordered (default: 1)
                    - id (str): Unique item identifier
                    - order_id (str): ID of the parent order
                    - product_id (str): ID of the product
                    - product_variant_id (str): ID of the product variant

        On error, returns CallToolResult with error details if the MemCommerce API
        request fails or if there are connectivity issues.
    """
    try:
        orders_data = await get_user_orders(user_jwt)
    except MemCommerceAPIException as e:
        return CallToolResult(
            isError=True,
            content=[TextContent(type="text", text=f"MemCommerce API Error: {e}")],
        )

    return orders_data
