import pytest
import requests

@pytest.fixture(scope="session")
def base_url():
    """Базовый URL запущенного Nginx. Используется во всех тестах."""
    return "http://localhost:8080"

@pytest.fixture(scope="session")
def session():
    """Создаёт одну сессию HTTP-запросов для всех тестов (экономит ресурсы)."""
    session = requests.Session()
    yield session
    session.close()