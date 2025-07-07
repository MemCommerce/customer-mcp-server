from pydantic import BaseModel, EmailStr


class Order(BaseModel):
    full_name: str
    email: EmailStr
    address: str
    city: str
    country: str
    status: str
    id: str
    user_id: str


class OrderItem(BaseModel):
    name: str
    image_url: str | None = None
    price: float
    quantity: int = 1
    id: str
    order_id: str
    product_id: str
    product_variant_id: str


class OrderData(BaseModel):
    order: Order
    order_items: list[OrderItem]


class OrderListData(BaseModel):
    data: list[OrderData]
