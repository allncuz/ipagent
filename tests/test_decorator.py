import pytest
from unittest.mock import AsyncMock, patch, Mock
from starlette.requests import Request
from ipagent import ClientInfo, request_info


@pytest.mark.asyncio
@patch("ipagent.internal.decorators.get_client_info", new_callable=AsyncMock)
async def test_request_info_decorator(get_client_info_mock):
    mock_client_info = ClientInfo(
        ip_client="203.0.113.195",
        device_type="Mobile",
        browser="Safari",
        browser_version="14.0",
        os="iOS",
        os_version="14.0",
        country="UZ",
        region="Tashkent Region",
        city="Tashkent",
        latitude=41.3111,
        longitude=69.2797,
        timezone="Asia/Tashkent",
        postal="100000",
        org="Uztelecom"
    )

    get_client_info_mock.return_value = mock_client_info

    @request_info
    async def endpoint(request: Request, user_info: ClientInfo):
        return {"ip": user_info.ip_client, "device": user_info.device_type}

    mock_request = Mock(spec=Request)
    mock_request.headers = {
        "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X)",
        "x-forwarded-for": "203.0.113.195",
    }
    mock_request.client.host = "127.0.0.1"

    result = await endpoint(mock_request)

    assert result["ip"] == "203.0.113.195"
    assert result["device"] == "Mobile"
    get_client_info_mock.assert_called_once_with(mock_request)
