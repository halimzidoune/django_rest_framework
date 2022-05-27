import requests

#endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/"

response = requests.get(endpoint, params={"name": "josef"}, json={"query": "Hello"})

# print(response.text)
print(response.json())
#print(response.json()["message"])
print(response.status_code)

