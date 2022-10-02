import app.teams_show.router as team_api
import app.user.router as user_api
import app.tracks_show.router as track_api
from app.contracts.user_contract import User
from app.contracts.team_contract import Team
from app.contracts.track_contract import Track


def test_user_team():
    """
    we create new user, create new team and add this user to team.
    :return:
    """
    test_user = User(name="bob", mail="some@mail", skills=["one", "two"])
    test_user_2 = User(name="jack", mail="another@mail", skills=["one", "two"])
    test_team = Team(name="test", track="test", members=[test_user])
    user_api.registration(test_user_2)
    team_api.create_new_team(test_team)
    teams = team_api.get_all_teams()["teams"]
    team_api.join_the_team(test_user_2, len(teams))
    teams = team_api.get_all_teams()["teams"]
    assert test_user_2 in teams[len(teams)]['members']
