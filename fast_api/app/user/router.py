from app.contracts.user_contract import User
from fastapi import APIRouter
from typing import List
import db.db_interface as db_int

router = APIRouter(prefix='/user')


def check_user_data(user: User) -> bool:
    return True


def check_user_exist(user: User) -> bool:
    return bool(db_int.get(object="User", instance=user))


def get_all_users_from_db() -> dict:
    return db_int.get_all("User")


@router.post("/reg")
def registration(user: User) -> dict:
    """
    Endpoint for new user registration
    :param user:
    :return:
    """
    try:

        if check_user_data(user) and not check_user_exist(user):
            db_int.post(object="User", instance=user)
        return {"Successfully created user": user.name}
    except Exception as ex:
        return {"Error": str(ex)}


@router.get("/all")
def get_list_of_users() -> dict:
    """
    Endpoint for getting list of all users.
    :return:
    """
    try:
        return {"Users": get_all_users_from_db()}

    except Exception as ex:
        return {"Error": str(ex)}
