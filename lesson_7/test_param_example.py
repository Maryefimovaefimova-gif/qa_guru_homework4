import pytest


@pytest.mark.parametrize(
    "auth_headers",
    ["User", "Admin", "Guest"],
    indirect=True,
    ids=["user_role", "admin_role", "guest_role"]
)
def test_api_authorization(auth_headers, api_client):
    print(f"\nТестирование с ролью: {auth_headers.get('X-User-Role')}")

    response = api_client.get("/users/profile")

    expected_role = auth_headers.get("X-User-Role")
    assert response["user_role"] == expected_role
    assert response["status"] == 200

    if expected_role == "admin":
        admin_response = api_client.post("/admin/users", data={"action": "create"})
        assert admin_response["status"] == 201
        print("  Админский доступ подтвержден")

    if expected_role == "guest":
        guest_response = api_client.get("/users/9999/profile")
        assert guest_response["status"] == 200
        print("  Гостевой доступ подтвержден")
