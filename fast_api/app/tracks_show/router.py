from app.contracts.user_contract import User
from app.contracts.team_contract import Team
from app.contracts.track_contract import Track
from fastapi import APIRouter
from typing import List
import db.db_interface as db_int

router = APIRouter(prefix='/tracks')


def get_track_by_id(track_id: int) -> Track:
    return db_int.get(object="Track", id=track_id)


def add_team_to_track(team: Team, track_id: int):
    db_int.put(object_where="Track", object_field="teams", action="append", where_id=track_id, data=team)


def check_track_exist(new_track):
    return False


@router.get('/all')
def get_all_tracks() -> dict:
    """
    Endpoint for getting list of all tracks
    :return:
    """
    try:
        return {"tracks": db_int.get_all("Track")}
    except Exception as ex:
        return {"Error": str(ex)}


@router.get('/{track_id}')
def get_track_info(track_id: int) -> dict:
    """
    Endpoint for getting specific info about track
    :param track_id:
    :return:
    """
    try:
        return {"track": get_track_by_id(track_id)}
    except Exception as ex:
        return {"Error": str(ex)}


@router.post('/{track_id}/add_team')
def post_team_to_track(team: Team, track_id: int) -> dict:
    """
    Endpoint for adding new_team to existing track
    :param track_id:
    :param team:
    :return:
    """
    try:
        add_team_to_track(team, track_id)
    except Exception as ex:
        return {"Error": str(ex)}


@router.post('/new')
def create_new_track(new_track: Track):
    """
        Endpoint for creating new team
        :return:
        """
    try:
        if not check_track_exist(new_track):
            db_int.post(object="Track", instance=new_track)
    except Exception as ex:
        return {"Error": str(ex)}
