from ghapi.all import GhApi
from dotenv import dotenv_values
from pprint import pprint
import base64

env = dotenv_values('.env')
github_token = env.get('GH_TOKEN')

# api = GhApi(owner='DeeJaeMann', repo='careercompass', token=github_token)
api = GhApi(owner="Code-Platoon-Curriculum", repo="curriculum", token=github_token)

# pprint(api.repos.get())
# pprint(base64.b64decode(api.repos.get_readme()['content']).decode())
pprint(api.markdown.render_raw(base64.b64decode(api.repos.get_readme()['content']).decode()))
