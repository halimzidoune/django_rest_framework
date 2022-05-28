from urllib import response
import requests

endpoint_product = "http://localhost:8000/api/products/1/update/"

data = {
    "title" : "Modified Title"
}

response = requests.put(endpoint_product, json=data)

print(response.json())
