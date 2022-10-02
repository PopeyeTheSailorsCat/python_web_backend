import pytest
import app.teams_show.router as team_api
from app.contracts.user_contract import User
from app.contracts.team_contract import Team

test_user = User(name="bob", mail="some@mail", skills=["one", "two"])


def test_get_all():
    resp = team_api.get_all_teams()
    assert len(resp["teams"]) == 1  # DEFAULT TEST DB VALUE


def test_create_new_team():
    team = Team(name="test", track="test", members=[test_user])
    teams = team_api.get_all_teams()["teams"]
    size_1 = len(teams)
    assert team not in teams.values()
    team_api.create_new_team(team)
    teams = team_api.get_all_teams()["teams"]
    assert len(teams) - 1 == size_1
    assert team in teams.values()  # TODO


def test_join_team():
    teams = team_api.get_all_teams()["teams"]
    assert test_user not in teams[1]["members"]  # user dont in db
    team_api.join_the_team(test_user, 1)
    teams = team_api.get_all_teams()["teams"]
    assert test_user in teams[1]["members"]  # user in db
