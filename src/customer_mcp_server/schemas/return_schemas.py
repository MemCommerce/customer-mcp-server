from pydantic import BaseModel


class ReturnBase(BaseModel):
    status: str
    reason: str
    order_id: str


class ReturnCreate(ReturnBase):
    pass


class Return(ReturnBase):
    id: str
    user_id: str


class ReturnItemBase(BaseModel):
    quantity: int
    reason: str | None = None
    order_item_id: str


class ReturnItemCreate(ReturnItemBase):
    pass


class ReturnItem(ReturnItemBase):
    id: str
    return_id: str


class ReturnDataCreate(BaseModel):
    return_request: ReturnCreate
    items: list[ReturnItemCreate]


class ReturnData(BaseModel):
    return_request: Return
    items: list[ReturnItem]
