import requests

a = requests.get('path/to/forest.jpg, stream=True')
req.raise_for_status()
with open('Forest.jpg', 'wb') as fd:
    for chuck in req.iter_content(chunk_size=5000):
        print('Received a Chunk')
        fd.write(chunk)
