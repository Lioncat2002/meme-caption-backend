import requests
import base64
import pickle
url = f"https://memer-ai.herokuapp.com/upload/"
url = "http://127.0.0.1:8000/upload/"
file = {"file": base64.urlsafe_b64encode(open("images/noita.jpg", "rb").read())}
resp = requests.post(url=url, files=file)
print(resp.text)
