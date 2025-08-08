from typing import Union

from modular_mcp.bundle import Bundle
from mcp.types import CallToolResult, TextContent

from exceptions import MemCommerceAPIException
from schemas.email_schemas import EmailDetails
from api.email_api import post_email



bundle = Bundle()


@bundle.tool()
async def send_email(details: EmailDetails) -> Union[None, CallToolResult]:
    """
    Sends an email to a user using the provided details.

    This Model Context Protocol tool attempts to send an email with the specified subject and content to
    the user identified by `user_id`. If the operation succeeds, the function returns `None`. If an error occurs
    during the process (such as a MemCommerce API exception), a `CallToolResult` is returned with error details.

    Args:
        details (EmailDetails): Information required to construct and send the email.

    Returns:
        None: If the email is sent successfully.
        CallToolResult: If an error occurs, containing information about the failure.

    Example:
        details = EmailDetails(
            user_id="123456",
            subject="Order Confirmation",
            content="Your order has been placed successfully."
        )
        await send_email(details)
    """
    try:
        await post_email(details)
    except MemCommerceAPIException as e:
        return CallToolResult(
            isError=True,
            content=[TextContent(type="text", text=f"MemCommerce API Error: {e}")],
        )
