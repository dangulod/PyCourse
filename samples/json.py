import requests

r = requests.get("https://api.github.com/users?since=100")

r.json()
