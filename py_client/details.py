from urllib import response
import requests

endpoint_product = "http://localhost:8000/api/products/1/"

response = requests.get(endpoint_product)

print(response.json())
