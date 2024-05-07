from ghapi.all import GhApi
from dotenv import dotenv_values
from pprint import pprint, pformat
import base64
import re

env = dotenv_values('.env')
github_token = env.get('GH_TOKEN')

# api = GhApi(owner='DeeJaeMann', repo='careercompass', token=github_token)
api = GhApi(owner="Code-Platoon-Curriculum", repo="curriculum", token=github_token)

cp_curr = api.repos
cp_curr_repo = cp_curr.get()
cp_curr_url = cp_curr_repo['owner']['html_url']
cp_curr_readme = cp_curr.get_readme()
cp_curr_readme_url = cp_curr_readme['_links']['html']
cp_curr_content = cp_curr.get_content(path="/")

cp_curr_teams = api.teams.list(org='Code-Platoon-Curriculum')
# team_whiskey = cp_curr_teams[]
for team in cp_curr_teams:
    # print(team['name'])
    if team['name'] == 'whiskey_students':
        whiskey_team = team

for dir in cp_curr_content:
    print(dir['name'])
    if re.match(r'^1', dir['name']):
        wkone_dir = dir
    elif re.match(r'^2', dir['name']):
        wktwo_dir = dir
    elif re.match(r'^3', dir['name']):
        wkthree_dir = dir

wkone_path = wkone_dir['path']
wkone_content = cp_curr.get_content(path=wkone_path)
wkone_readme = cp_curr.get_readme_in_directory(dir=wkone_path)
wkone_readme_url = wkone_readme['html_url']
# wkone_readme = wkone_content.get_readme()

print(f"***ReadmeUrl***")
pprint(cp_curr_readme_url)

# wkone_pattern = r'^1'

# pprint(cp_curr.get_readme_in_directory())

# pprint(cp_curr.get_pages(owner='Code-Platoon-Curriculum', repo='curriculum'))

# pprint(pformat(cp_curr_content))

print(f"***Week One Path***")
print(wkone_path)

print(f"***Week One Dir***")
pprint(wkone_dir)

print(f"***Week One Content")
pprint(pformat(wkone_content))

print(f"***Week One Readme***")
pprint(wkone_readme_url)

# pprint(cp_curr.) get topics

# pprint(pformat(api.teams.list(org='Code-Platoon-Curriculum', indent=2)))
# pprint(cp_curr_teams)
# pprint(api.repos.get_readme())
# pprint(base64.b64decode(api.repos.get_readme()['content']).decode())
# pprint(api.markdown.render_raw(base64.b64decode(api.repos.get_readme()['content']).decode()))
# pprint(whiskey_team)
