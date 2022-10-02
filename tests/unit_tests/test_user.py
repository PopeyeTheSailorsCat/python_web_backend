import pytest
import app.user.router as user_api
from app.contracts.user_contract import User


def test_user_all_list():
    db_length = len(user_api.get_all_users_from_db())
    assert db_length == 1  # DEFAULT TEST DB VALUE


def test_user_registration():
    db_length = len(user_api.get_all_users_from_db())
    user = User(name="bob", mail="some@mail", skills=["one", "two"])
    resp = user_api.registration(user)
    assert "Error" not in list(resp.keys())
    db_length_2 = len(user_api.get_all_users_from_db())
    assert db_length == db_length_2 - 1
