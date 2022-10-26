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


def test_team_track():
    """
    we create new team, new track and add new team to new track.
    :return:
    """
    test_user = User(name="bob", mail="some@mail", skills=["one", "two"])
    test_team = Team(name="test", track="test", members=[test_user])
    test_track = Track(name='test track', description='my little track', teams=[test_team])
    test_team_2 = Team(name="another_Test", track="test", members=[test_user])
    track_api.create_new_track(test_track)
    team_api.create_new_team(test_team)
    new_track_id = len(track_api.get_all_tracks()["tracks"])
    track_api.post_team_to_track(test_team_2, track_id=new_track_id)
    assert test_team_2 in track_api.get_track_by_id(new_track_id)["teams"]


def test_list_of_all_users_and_team():
    """
    find user what is not member of the team and add this user to team
    :return:
    """
    users = user_api.get_list_of_users()["Users"]
    teams = team_api.get_all_teams()["teams"]
    working_team = None
    working_user = None
    for user in users.values():
        for team_id, team in teams.items():
            if user not in team["members"]:
                working_team = team_id
                working_user = user
    if working_user and working_team:
        team_api.join_the_team(working_user, working_team)
        current_team = team_api.get_all_teams()["teams"][working_team]
        assert working_user in current_team["members"]
