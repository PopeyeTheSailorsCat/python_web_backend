from app.contracts.user_contract import User
from app.contracts.team_contract import Team
from app.contracts.track_contract import Track
import app.tracks_show.router as track_api

test_user = User(name="bob", mail="some@mail", skills=["one", "two"])
test_team = Team(name="test", track="test", members=[test_user])


def test_get_all_tracks():
    tracks = track_api.get_all_tracks()["tracks"]
    assert len(tracks) == 1  # default test DB value


def test_get_track_info():
    resp = track_api.get_track_by_id(1)
    assert resp["name"] == "track_name"  # default test NAME


def test_post_team_to_track():
    len_1 = len(track_api.get_track_by_id(1)["teams"])
    track_api.post_team_to_track(test_team, 1)
    len_2 = len(track_api.get_track_by_id(1)["teams"])
    assert len_1+1 == len_2
