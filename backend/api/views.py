import imp
from logging import raiseExceptions
from pickle import TRUE
# from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.forms.models import model_to_dict
import json
from products.models import Product

from products.serializers import ProductSerializer

@api_view(['POST'])
def product(request, *args, **kwargs):
    
    serializer = ProductSerializer(data = request.data)
    if serializer.is_valid(raise_exception = TRUE):
        serializer.save()
        data = serializer.data
        return Response(data)
    else:
        return Response({"error": "Invalid Data"}, status = 400)

# @api_view(["GET"])
# def product(request, *args, **kwargs):
#     product = Product.objects.all().order_by("?").first()

#     data = {}
    
#     if product:
#         # data = model_to_dict(product)
        
#         # data = model_to_dict(product, fields=['title', 'price', 'sale_price']) # doesn'nt work
#         data = ProductSerializer(product).data
#         return Response(data)


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

