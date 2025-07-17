from typing import Union


from modular_mcp.bundle import Bundle
from mcp.types import CallToolResult, TextContent

from schemas.return_schemas import ReturnData, ReturnDataCreate
from exceptions import MemCommerceAPIException
from api.return_api import post_user_return, get_user_returns


bundle = Bundle()


@bundle.tool()
async def create_user_return(
    data: ReturnDataCreate, user_jwt: str
) -> Union[ReturnData, CallToolResult]:
    """
    Submit a return request for a user's order.

    This function allows the user to initiate a return request by providing the order ID,
    reason for return, and the list of items to be returned along with their quantities.
    It uses the provided JWT token for authentication and submits the data to the MemCommerce API.

    Args:
        data (ReturnDataCreate): A ReturnDataCreate object containing:
            - return_request (ReturnCreate): Metadata for the return request, including:
                - status (str): Current status of the return request (e.g., "pending", "approved").
                - reason (str): Reason provided by the user for the return.
                - order_id (str): ID of the order being returned.
            - items (list[ReturnItemCreate]): A list of return items, where each item includes:
                - quantity (int): Quantity of the item being returned.
                - reason (str | None): Optional reason specific to this item.
                - order_item_id (str): ID of the order item being returned.

        user_jwt (str): JSON Web Token (JWT) for authenticating the user making the return.

    Returns:
        Union[ReturnData, CallToolResult]: A ReturnData object containing:
            - return_request (Return): Metadata of the return request, including:
                - id (str): Unique identifier for the return request.
                - status (str): Status of the return request.
                - reason (str): Reason provided by the user.
                - order_id (str): ID of the associated order.
                - user_id (str): ID of the user who submitted the return.
            - items (list[ReturnItem]): List of returned items, each containing:
                - id (str): Unique identifier for the returned item.
                - quantity (int): Quantity of the item being returned.
                - reason (str | None): Optional item-specific reason for the return.
                - order_item_id (str): ID of the original order item.
                - return_id (str): ID of the associated return request.

        On error, returns CallToolResult with error details if the MemCommerce API
        request fails or if there are connectivity/authentication issues.
    """
    try:
        return_data = await post_user_return(data, user_jwt)
    except MemCommerceAPIException as e:
        return CallToolResult(
            isError=True,
            content=[TextContent(type="text", text=f"MemCommerce API Error: {e}")],
        )

    return return_data


@bundle.tool()
async def list_all_user_returns(
    user_jwt: str,
) -> Union[list[ReturnData], CallToolResult]:
    """
    Retrieve all return requests submitted by the user.

    This function fetches all return requests associated with the provided user JWT token.
    Each return includes information about the return reason, order, status, and the
    items being returned. It is useful for allowing users to view their return history
    within the system.

    Args:
        user_jwt (str): JSON Web Token (JWT) for authenticating the user making the request.

    Returns:
        Union[list[ReturnData], CallToolResult]: A list of ReturnData objects, where each ReturnData contains:
            - return_request (Return): Metadata for the return request, including:
                - id (str): Unique identifier for the return request.
                - status (str): Status of the return (e.g., "pending", "approved").
                - reason (str): Reason for the return.
                - order_id (str): ID of the associated order.
                - user_id (str): ID of the user who submitted the return.
            - items (list[ReturnItem]): List of items associated with the return, where each item includes:
                - id (str): Unique identifier for the returned item.
                - quantity (int): Quantity being returned.
                - reason (str | None): Optional item-specific reason for return.
                - order_item_id (str): ID of the original order item.
                - return_id (str): ID of the parent return request.

        On error, returns CallToolResult with error details if the MemCommerce API
        request fails or if there are connectivity/authentication issues.
    """
    try:
        returns_datas = await get_user_returns(user_jwt)
    except MemCommerceAPIException as e:
        return CallToolResult(
            isError=True,
            content=[TextContent(type="text", text=f"MemCommerce API Error: {e}")],
        )

    return returns_datas
