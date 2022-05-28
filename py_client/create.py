from urllib import response
import requests

endpoint_product = "http://localhost:8000/api/products/"

data = {
    "title": "new title",
    "content": "Hello",
    "price": 123.00
}
response = requests.post(endpoint_product, json=data)

print(response.json())
