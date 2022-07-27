import requests

headers = {
    'accept': 'application/json',
    'content-type': 'application/x-www-form-urlencoded',
}

params = {
    'data': 'hellow',
}

response = requests.post('http://127.0.0.1:8000/encoded/', params=params, headers=headers)
print(response.json())