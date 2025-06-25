from typing import Union

from mcp.types import CallToolResult, TextContent
from modular_mcp.bundle import Bundle

from schemas.storefront_schemas import StorefrontData
from api.storefront import get_hole_storefront
from exceptions import MemCommerceAPIException


bundle = Bundle()


@bundle.tool()
async def list_hole_storefront_data() -> Union[StorefrontData, CallToolResult]:
    """
    Retrieve complete storefront data from the MemCommerce system for display purposes.

    This function fetches all publicly available product information that would typically
    be displayed on an e-commerce storefront, including products with their variants,
    pricing, and categorization. The data returned is structured for front-end display
    and customer browsing experiences.

    The storefront data includes:
    - All active products with their basic information (name, brand, description)
    - Product categorization for navigation and filtering
    - Complete variant information including size and color options
    - Current pricing for each product variant
    - Relationships between products and their available variants

    This is ideal for:
    - Building product catalogs and listings
    - Implementing product search and filtering
    - Displaying product details with available options
    - Price comparison and inventory analysis
    - Creating storefront mockups or demos

    Returns:
        Union[StorefrontData, CallToolResult]: A StorefrontData object containing:
            - products: List of StorefrontProduct objects, each containing:
                - id: Unique product identifier
                - name: Product display name
                - brand: Product brand/manufacturer
                - description: Product description text
                - category_name: Category for organization/filtering
                - variants: List of StorefrontVariant objects with:
                    - id: Unique variant identifier
                    - size/size_id: Size option and its ID
                    - color/color_id: Color option and its ID
                    - price: Current price for this specific variant

        On error, returns CallToolResult with error details if the MemCommerce API
        request fails or if there are connectivity issues.
    """
    try:
        storefront_data = await get_hole_storefront()
    except MemCommerceAPIException as e:
        return CallToolResult(
            isError=True,
            content=[TextContent(type="text", text=f"MemCommerce API Error: {e}")],
        )

    return storefront_data
