import requests
import base64
from PIL import Image
headers = {
    'accept': 'application/json',
    # Already added when you pass json= but not when you pass data=
    # 'Content-Type': 'application/json',
}
s=base64.b64encode(open("images/noita.jpg","rb").read())

json_data = {
    'data': s.decode('utf-8'),
}

response = requests.post('http://127.0.0.1:8000/encoded/', headers=headers, json=json_data)
print(response.text)
