import imp
from django.http import JsonResponse
import json
from products.models import Product

def product(request, *args, **kwargs):
    product = Product.objects.all().order_by("?").first()

    data = {}
    
    if product:
        data['id'] = product.id
        data['title'] = product.title
        data['price'] = product.price
        data['content'] = product.content
        return JsonResponse(data)


def api_home(request, *args, **kwargs):
    data = {}
    body = request.body
    
    print(body)

    try:
        data = json.loads(body)
    except:
        pass

    # print(data.keys())  # -> show params names sended in json
    print(request.headers)
    data['content_type'] = request.content_type
    data['headers'] = dict(request.headers)
    data['params'] = request.GET
    data['name'] = request.GET['name']

    return JsonResponse(data)

