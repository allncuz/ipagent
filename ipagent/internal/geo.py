import httpx

IPAPI_URL = "https://ipapi.co/{ip}/json/"


async def fetch_geo(ip: str) -> dict:
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(IPAPI_URL.format(ip=ip), timeout=5.0)
            data = response.json()
            return {
                "country": data.get("country_name"),
                "region": data.get("region"),
                "city": data.get("city"),
                "latitude": data.get("latitude"),
                "longitude": data.get("longitude"),
                "timezone": data.get("timezone"),
                "postal": data.get("postal"),
                "org": data.get("org"),
            }
    except Exception:
        return {}
