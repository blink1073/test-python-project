import os

from ghapi.core import GhApi

gh = GhApi("blink1073", "test-python-project")
user = os.environ["ACTOR"]
collab_level = gh.repos.get_collaborator_permission_level(user)
print(collab_level["permission"] == "admin")
