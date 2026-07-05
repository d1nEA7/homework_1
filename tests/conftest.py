import os
from unittest.mock import patch

import pytest


@pytest.fixture(autouse=True, scope="session")
def set_env():
    os.environ["API_KEY"] = "some-secret-key"


@pytest.fixture
def mocked_request_get():
    with patch("requests.get") as mock:
        yield mock
