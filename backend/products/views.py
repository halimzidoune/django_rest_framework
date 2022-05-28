import imp
from rest_framework import generics

from .models import Product
from .serializers import ProductSerializer

class ProductDetailsAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'pk'
