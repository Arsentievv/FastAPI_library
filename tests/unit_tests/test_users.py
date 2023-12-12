from starlette.testclient import TestClient
import pytest
from fastapi import status

from src.main import app
from src.users import crud


@pytest.fixture(scope='class')
def empty_users():
    crud.delete_all()


@pytest.mark.usefixtures("empty_users")
class TestUsers:

    def test_user_creation(self):
        client = TestClient(app)
        url = '/create-user/'
        testing_data = {
            "username": "test_username1",
            "email": "test_email1@test.ru",
            "full_name": "test_full_name",
            "password": "test_password"
        }
        response = client.post(url, json=testing_data)
        assert response.status_code == status.HTTP_200_OK
