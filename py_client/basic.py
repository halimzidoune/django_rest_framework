from urllib import response
import requests

#endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/"

endpoint_product = "http://localhost:8000/api/product/"

response = requests.post(endpoint_product, json={"title": "New Product", "content": "Content 1", "price": 100.00})
# response = requests.get(endpoint_product) # Get Product Randomly 

print(response.json())

# response = requests.get(endpoint, params={"name": "josef"}, json={"query": "Hello"})

# # print(response.text)
# print(response.json())
# #print(response.json()["message"])
# print(response.status_code)

