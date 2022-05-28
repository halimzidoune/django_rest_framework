from urllib import response
import requests

endpoint_product = "http://localhost:8000/api/products/3/delete"

response = requests.delete(endpoint_product)

print(response.status_code)
