from functools import wraps
from fastapi import Request
from ipagent.internal.client import get_client_info
from ipagent.internal.types import ClientInfo


def request_info(func):
    @wraps(func)
    async def wrapper(request: Request, *args, **kwargs):
        user_info: ClientInfo = await get_client_info(request)
        return await func(request, user_info=user_info, *args, **kwargs)

    return wrapper
