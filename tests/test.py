import requests

url = "https://memer-ai.herokuapp.com/upload/mrow"
url = "http://127.0.0.1:8000/upload/mrow"
#file = {"file": open("images/noita.jpg", "rb")}
resp = requests.get(url=url)
print(resp.json())
