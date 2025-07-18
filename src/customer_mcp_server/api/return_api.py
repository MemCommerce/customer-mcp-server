from config import API_URL
from api.common import safe_request
from schemas.return_schemas import ReturnDataCreate, ReturnData


async def get_user_returns(user_jwt: str) -> list[ReturnData]:
    url = f"{API_URL}/returns/"
    headers = {"Authorization": f"Bearer {user_jwt}"}
    returns_resp = await safe_request("GET", url, headers=headers)
    returns_datas = [ReturnData(**r) for r in returns_resp]
    return returns_datas


async def post_user_return(data: ReturnDataCreate, user_jwt: str) -> ReturnData:
    url = f"{API_URL}/returns/"
    headers = {"Authorization": f"Bearer {user_jwt}"}
    body = data.model_dump()
    returns_resp = await safe_request("POST", url, headers=headers, json=body)
    return_data = ReturnData(**returns_resp)
    return return_data
