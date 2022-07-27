import requests
import base64
import pickle
print(requests.get("https://memer-ai.herokuapp.com/").json())
#url = "https://memer-ai.herokuapp.com/upload/"
img=base64.urlsafe_b64encode(open("images/noita.jpg","rb").read())
url = f"http://127.0.0.1:8000/encoded/{img}"
#file = {"file": open("images/noita.jpg", "rb")}
resp = requests.get(url=url)
print(resp.text)
