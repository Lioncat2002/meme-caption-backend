import requests

url = "https://memer-ai.herokuapp.com/upload/"
# url = "http://127.0.0.1:8000/upload/"
file = {"file": open("images/noita.jpg", "rb")}
resp = requests.post(url=url, files=file)
print(resp.json())
