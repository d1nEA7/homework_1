import pytest

from src.external_api import convert_currency


@pytest.mark.usefixtures("mocked_request_get")
def test_fuo(mocked_request_get):
    result = convert_currency(10.0, "USD")
