#api que me retorna personajes

import requests

data = requests.get("https://rickandmortyapi.com/api/character")

print(data.text)

#nombre = input('Dame el nombre de un personaje de rick y morty:')


