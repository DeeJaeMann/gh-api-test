from github import Github
from github import Auth
import base64
from pprint import pprint
from dotenv import dotenv_values
from jwt import JWT, jwk

env = dotenv_values('.env')
username = env.get('USERNAME')

# auth = Auth.Token