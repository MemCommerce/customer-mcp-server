from modular_mcp.modular_mcp import ModularFastMCP
from bundles import storefront_bundle, order_bundle

mcp = ModularFastMCP("MemCommerce Customer MCP server")
mcp.include_bundle(storefront_bundle.bundle)
mcp.include_bundle(order_bundle.bundle)


def main():
    mcp.run(transport="streamable-http")


if __name__ == "__main__":
    main()
