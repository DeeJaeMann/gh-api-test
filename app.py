import requests
from pprint import pprint
from dotenv import dotenv_values

env = dotenv_values('.env')

username = env.get('USERNAME')
url = f'https://api.github.com/users/{username}'
response = requests.get(url)

if response.ok:
    data = response.json()
    pprint(data)
else:
    print(f'Request failed with status code {response.status_code}')