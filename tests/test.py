import requests

url = "https://memer-ai.herokuapp.com/upload/"
file = {"file": open("images/noita.jpg", "rb")}
resp = requests.post(url=url, files=file)
print(resp.json())
