from urllib import response
import requests

endpoint_product = "http://localhost:8000/api/products/10/delete"

response = requests.delete(endpoint_product)

print(response.json())
