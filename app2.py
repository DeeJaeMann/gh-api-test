from github import Github
import base64
from pprint import pprint
from dotenv import dotenv_values

env = dotenv_values('.env')
username = env.get('USERNAME')
gh = Github()

def print_repo(repo):
    pprint(f'Full name: {repo.full_name}')
    pprint(f'Descriptoin: {repo.description}')
    pprint(f'Home Page: {repo.homepage}')

    pprint('Contents:')
    for content in repo.get_contents(""):
        try:
            pprint(content)
        except:
            pass

user = gh.get_user(username)

for repo in user.get_repos():
    print_repo(repo)
