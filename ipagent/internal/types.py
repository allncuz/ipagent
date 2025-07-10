from pydantic import BaseModel
from typing import Optional


class ClientInfo(BaseModel):
    ip_client: str
    device_type: str
    browser: str
    browser_version: str
    os: str
    os_version: str
    country: Optional[str]
    region: Optional[str]
    city: Optional[str]
    latitude: Optional[float]
    longitude: Optional[float]
    timezone: Optional[str]
    postal: Optional[str]
    org: Optional[str]
