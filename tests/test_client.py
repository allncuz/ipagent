import pytest
from unittest.mock import patch, AsyncMock, Mock
from starlette.datastructures import Headers
from ipagent import ClientInfo, get_client_info


@pytest.mark.asyncio
@patch("ipagent.internal.client.fetch_geo", new_callable=AsyncMock)
async def test_get_client_info_direct(fetch_geo_mock):
    fetch_geo_mock.return_value = {
        "country": "UZ",
        "region": "Tashkent Region",
        "city": "Tashkent",
        "latitude": 41.3111,
        "longitude": 69.2797,
        "timezone": "Asia/Tashkent",
        "postal": "100000",
        "org": "Uztelecom"
    }

    mock_request = Mock()
    mock_request.headers = Headers({
        "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X)",
        "x-forwarded-for": "203.0.113.195",
    })
    mock_request.client.host = "127.0.0.1"

    result: ClientInfo = await get_client_info(mock_request)

    assert isinstance(result, ClientInfo)
    assert result.ip_client == "203.0.113.195"
    assert result.device_type == "Mobile"
    assert result.country == "UZ"
    assert result.city == "Tashkent"
    assert result.region == "Tashkent Region"
    assert result.org == "Uztelecom"
