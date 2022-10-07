from app.contracts.user_contract import User
from app.contracts.team_contract import Team
from app.contracts.track_contract import Track

basic_user = {"name": "name", "mail": "mail", "skills": ["skill_1", "skill_2"]}
another_user = {"name": "John", "mail": "my@mail", "skills": ["live", "talk"]}
basic_team = {"name": "team_name", "track": "track", "members": [basic_user]}
USERS = {1: basic_user, 2:another_user}
TEAMS = {1: basic_team}
TRACKS = {1: {"name": "track_name", "description": "something", "teams": [basic_team]}}
db = {"Team": TEAMS, "User": USERS, "Track": TRACKS}


def get(*args, **kwargs):
    if "id" in kwargs:
        return db[kwargs['object']][kwargs["id"]]

    # else:
    # return db[kwargs['object']]


def post(*args, **kwargs):
    class_name = kwargs['object']
    instance = kwargs['instance']
    # print(db.keys()) )
    db[class_name][len(db[class_name]) + 1] = vars(instance)


def get_all(*args, **kwargs):
    return db[args[0]]


def put(*args, **kwargs):
    put_class = kwargs['object_where']
    put_field = kwargs['object_field']
    put_action = kwargs['action']
    if put_action == "append":
        if kwargs["where_id"]:
            db[put_class][kwargs['where_id']][put_field].append(kwargs["data"])
