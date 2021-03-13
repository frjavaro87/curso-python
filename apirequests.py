import requests

data = requests.get("https://jsonplaceholder.typicode.com/todos/5")

if data.status_code == 200:
    data = data.text
    print(data)

else:
    print("hubo un error")