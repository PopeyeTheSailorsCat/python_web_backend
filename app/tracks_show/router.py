from app.contracts.user_contract import User
from app.contracts.team_contract import Team
from app.contracts.track_contract import Track
from fastapi import APIRouter
from typing import List
import db.db_interface as db_int

router = APIRouter(prefix='/tracks')


def get_track_by_id(track_id: int) -> Track:
    return db_int.get(object="Track", id=track_id)


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
def post_team_to_track(team: Team) -> dict:
    """
    Endpoint for adding new_team to existing track
    :param team:
    :return:
    """
    pass
