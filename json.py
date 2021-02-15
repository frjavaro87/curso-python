import requests as req

APIURL = "https://rickandmortyapi.com/api/character/1"

data = req.get(APIURL, allow_redirects = False)

print(data.text)