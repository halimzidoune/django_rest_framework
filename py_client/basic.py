import requests

endpoint = "https://httpbin.org/anything"

response = requests.get(endpoint)

# print(response.text)
print(response.json())
print(response.status_code)

