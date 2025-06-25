import os

from modular_mcp.modular_mcp import ModularFastMCP
from dotenv import load_dotenv
from bundles import storefront_bundle

load_dotenv()

API_URL = os.getenv("API_URL", "http://localhost:8001")

mcp = ModularFastMCP("MemCommerce Customer MCP server")
mcp.include_bundle(storefront_bundle.bundle)
