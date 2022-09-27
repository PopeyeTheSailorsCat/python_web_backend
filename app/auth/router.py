from app.contracts.user_contract import User
from fastapi import APIRouter
from typing import List
import db.db_interface as db_int

router = APIRouter(prefix='/auth')


def check_user_data(user: User):
    pass


def check_user_exist(user: User):
    return bool(db_int.get(user))


def create_user(user: User):
    db_int.post(user)


def get_all_users_from_db():
    pass


@router.post("/reg")
def registration(user: User) -> dict:
    try:
        check_user_data(user)
        if not check_user_exist(user):
            create_user(user)
        return {"Successfully created user": user.name}
    except Exception as ex:
        return {"Error": str(ex)}


@router.get("/all")
def get_list_of_users() -> dict:
    try:
        return {"Users": get_all_users_from_db()}

    except Exception as ex:
        return {"Error": str(ex)}
