import requests

url = "http://127.0.0.1:8000/generate"
data = {"prompt": "Hello world"}

response = requests.post(url, json=data)
print(response.json())
