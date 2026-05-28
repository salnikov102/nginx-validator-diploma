import pytest

def test_health_endpoint(base_url, session):
    """Проверка точки здоровья Nginx"""
    response = session.get(f"{base_url}/health")
    assert response.status_code == 200
    assert response.text.strip() == "OK"

def test_api_proxy(base_url, session):
    """Проверка проксирования запросов на бэкенд"""
    response = session.get(f"{base_url}/api/test")
    assert response.status_code == 200
    data = response.json()
    # Проверяем, что ответ пришёл от одного из наших бэкендов
    assert "backend-a" in data["message"] or "backend-b" in data["message"]

def test_backend_header(base_url, session):
    """Проверка наличия заголовка с именем сервера"""
    response = session.get(f"{base_url}/api/headers-check")
    assert response.status_code == 200
    assert "X-Backend-Server" in response.headers
    assert response.headers["X-Backend-Server"] in ["backend-a", "backend-b"]

   