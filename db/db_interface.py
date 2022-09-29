from app.contracts.user_contract import User
from app.contracts.team_contract import Team
from app.contracts.track_contract import Track

basic_user = {"name": "name", "mail": "mail", "skills": ["skill_1", "skill_2"]}
basic_team = {"name": "team_name", "track": "track", "members": [basic_user]}
USERS = {1: basic_user}
TEAMS = {1: basic_team}
TRACKS = {1: {"name": "track_name", "description": "something", "teams": [basic_team]}}
db = {"Team": TEAMS, "User": USERS, "Track": TRACKS}


def get(*args, **kwargs):
    if kwargs["id"]:
        return db[kwargs['object']][kwargs["id"]]


def post(*args, **kwargs):
    class_name = kwargs['object']
    instance = kwargs['instance']
    # print("here")
    db[class_name][len(db) + 1] = {"name": instance.name, "other": "Logic of bd here"}


def get_all(*args, **kwargs):
    return db[args[0]]
