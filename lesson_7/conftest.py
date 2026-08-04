import pytest


# ============= Задание 1: Indirect фикстура для авторизации =============
@pytest.fixture
def auth_headers(request):
    """
    Фикстура для косвенной параметризации заголовков авторизации.
    Получает роль из параметров и возвращает соответствующие заголовки.
    """
    role = request.param  # Получаем параметр из @pytest.mark.parametrize

    headers = {
        "User": {
            "Authorization": "Bearer user_token_123",
            "X-User-Role": "user",
            "X-User-Id": "1001"
        },
        "Admin": {
            "Authorization": "Bearer admin_token_456",
            "X-User-Role": "admin",
            "X-User-Id": "0001"
        },
        "Guest": {
            "Authorization": "Bearer guest_token_789",
            "X-User-Role": "guest",
            "X-User-Id": "9999"
        }
    }

    return headers.get(role, {})


@pytest.fixture
def api_client(auth_headers):
    """
    Фикстура, создающая API клиента с авторизационными заголовками.
    """

    class APIClient:
        def __init__(self, headers):
            self.headers = headers
            self.base_url = "https://api.example.com"

        def get(self, endpoint):
            print(f"  → GET {self.base_url}{endpoint}")
            print(f"  → Headers: {self.headers}")
            # Имитация ответа
            return {
                "status": 200,
                "data": f"Response from {endpoint}",
                "user_role": self.headers.get("X-User-Role", "unknown")
            }

        def post(self, endpoint, data=None):
            print(f"  → POST {self.base_url}{endpoint}")
            print(f"  → Headers: {self.headers}")
            print(f"  → Data: {data}")
            return {
                "status": 201,
                "message": "Created",
                "user_role": self.headers.get("X-User-Role", "unknown")
            }

    return APIClient(auth_headers)
