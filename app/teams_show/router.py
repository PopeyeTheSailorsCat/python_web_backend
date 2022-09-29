from app.contracts.user_contract import User
from app.contracts.team_contract import Team
from fastapi import APIRouter
from typing import List
import db.db_interface as db_int

router = APIRouter(prefix='/teams')


def add_user_to_team(user: User, team_id):
    pass


def check_new_team_data(new_team: Team) -> bool:
    return True


def team_exist(new_team: Team) -> bool:
    return False


@router.get("/all")
def get_all_teams() -> dict:
    """
    Endpoint to get list of all teams
    :return:
    """
    try:
        return {"teams": db_int.get_all("Team")}
    except Exception as ex:
        return {"Error": str(ex)}


@router.post("/{team_id}/join")
def join_the_team(user: User, team_id):
    """
    Endpoint for joining the team for user.
    :param user:
    :param team_id:
    :return:
    """
    try:
        add_user_to_team(user, team_id)
    except Exception as ex:
        return {"Error": str(ex)}


@router.post("/create")
def create_new_team(new_team: Team):
    """
    Endpoint for creating new team
    :param new_team:
    :return:
    """
    try:
        if check_new_team_data(new_team) and not team_exist(new_team):
            db_int.post(object="Team", instance=new_team)
    except Exception as ex:
        return {"Error": str(ex)}
