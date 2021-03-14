#api que me retorna personajes

import requests

original = "https://rickandmortyapi.com/api/character/?name="

nombre = input('Dame el nombre buscado: ')

search = original + nombre

data = requests.get(search)

print(data.text)