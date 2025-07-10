from fastapi import Request
from user_agents import parse
from ipagent.internal.types import ClientInfo
from ipagent.internal.geo import fetch_geo


async def get_client_info(request: Request) -> ClientInfo:
    ua = parse(request.headers.get("user-agent", ""))
    xff = request.headers.get("x-forwarded-for")
    ip = xff.split(',')[0] if xff else request.client.host

    geo = await fetch_geo(ip)

    return ClientInfo(
        ip_client=ip,
        device_type="Mobile" if ua.is_mobile else "Tablet" if ua.is_tablet else "Desktop",
        browser=ua.browser.family,
        browser_version=ua.browser.version_string,
        os=ua.os.family,
        os_version=ua.os.version_string,
        **geo
    )
