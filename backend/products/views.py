# from django.shortcuts import render

from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
# Create your views here.
# generic api view

class ProductsCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    def perform_create(self,serializer):
        # serializer.save(user = self.request.user)
        print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')
        
        if content is None:
            content = title

        serializer.save(content=content)
        # can send a signal
product_create_view = ProductsCreateAPIView.as_view()

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'pk'  #each model has one primary key by defualt 

product_detail_view = ProductDetailAPIView.as_view()

class ProductListAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'pk'  #each model has one primary key by defualt 

product_detail_view = ProductDetailAPIView.as_view()