import pytest

@pytest.fixture
def user():

    print("\nСоздаем пользователя")

    yield {
        "login": "admin",
        "password": "admin"
    }

    print("Удаляем пользователя")