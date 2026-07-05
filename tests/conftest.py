import os
from unittest.mock import patch

import pytest


@pytest.fixture(autouse=True, scope="session")
def set_env():
    """Устанавливает переменную окружения API_KEY для всех тестов."""
    os.environ["API_KEY"] = "some-secret-key"


@pytest.fixture
def mocked_request_get():
    """
    Фикстура, подменяющая requests.get на "мок".
    Используется в тестах для имитации ответов API без реальных запросов.
    """
    with patch("requests.get") as mock:
        yield mock
