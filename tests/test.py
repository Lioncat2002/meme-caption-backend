import requests
import base64
import pickle
print(requests.get("https://memer-ai.herokuapp.com/").json())
url = "https://memer-ai.herokuapp.com/upload/"
#url = "http://127.0.0.1:8000/upload/"
file = {"file": open("images/noita.jpg", "rb")}
resp = requests.post(url=url, files=file)
print(resp.text)
