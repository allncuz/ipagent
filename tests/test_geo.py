import pytest
from unittest.mock import patch
from ipagent import fetch_geo


@pytest.mark.asyncio
@patch("httpx.AsyncClient.get")
async def test_fetch_geo_success(mock_get):
    mock_get.return_value.json = lambda: {
        "country_name": "Uzbekistan",
        "region": "Tashkent Region",
        "city": "Tashkent",
        "latitude": 41.3111,
        "longitude": 69.2797,
        "timezone": "Asia/Tashkent",
        "postal": "100000",
        "org": "Uztelecom"
    }

    result = await fetch_geo("203.0.113.195")

    assert result["country"] == "Uzbekistan"
    assert result["region"] == "Tashkent Region"
    assert result["city"] == "Tashkent"
    assert result["latitude"] == 41.3111
    assert result["timezone"] == "Asia/Tashkent"
    assert result["org"] == "Uztelecom"


@pytest.mark.asyncio
@patch("httpx.AsyncClient.get", side_effect=Exception("network error"))
async def test_fetch_geo_failure(mock_get):
    result = await fetch_geo("203.0.113.195")
    assert result == {}
