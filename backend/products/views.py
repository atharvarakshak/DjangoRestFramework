# from django.shortcuts import render

from rest_framework import generics,mixins,permissions,authentication
from .models import Product
from .serializers import ProductSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .permissions import isStaffEditorPermission
from api.authentication import TokenAuthentication
# generic api view

class ProductsListCreateAPIView(generics.ListCreateAPIView):
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [
        authentication.SessionAuthentication,
        TokenAuthentication,
    ]
    permission_classes = [isStaffEditorPermission]

    def perform_create(self,serializer):
        # serializer.save(user = self.request.user)
        print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')
        
        if content is None:
            content = title

        instance = serializer.save(content=content)
        # can send a signal
product_list_create_view = ProductsListCreateAPIView.as_view()

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'pk'  #each model has one primary key by defualt 

product_detail_view = ProductDetailAPIView.as_view()

class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk' 

    def perform_update(self,serializer):
        instance = serializer.save() 
        if not instance.content:
            instance.content = instance.title

product_update_view = ProductUpdateAPIView.as_view()


class ProductDestroyAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk' 

    def perform_destroy(self,instance):
        super().perform_destroy(instance)

product_destroy_view = ProductDestroyAPIView.as_view()

# class ProductListAPIView(generics.RetrieveAPIView):
#     '''
#         not use
#     '''
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     # lookup_field = 'pk'  #each model has one primary key by defualt 

# product_list_view = ProductListAPIView.as_view()



#  combining ProductsListCreateAPIView & api_home into single view using
#  get and post conditions

# function based view are flexible but confusing

class ProductMixinView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    generics.GenericAPIView
    ):

    queryset = Product.objects.all()
    serializer_class= ProductSerializer
    lookup_field = 'pk'

    def get(self,request,*args,**kwargs):
        print(args,kwargs)
        pk=kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request,*args,**kwargs)
        return self.list(request,*args,**kwargs)
    
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
        
    def perform_create(self,serializer):
        # serializer.save(user = self.request.user)
        print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')
        
        if content is None:
            content = "this is a single wiew doing cool stuff"

        instance = serializer.save(content=content)
    
product_mixin_view = ProductMixinView.as_view()


@api_view(['GET','POST'])
def product_alt_view(request,pk=None,*args,**kwargs):
    method = request.method
    if method == "GET":
        if pk is not None:
            # detail view
            obj = get_object_or_404(Product,pk=pk)
            data = ProductSerializer(obj,many=False).data
            return Response(data)
    
         # list view
        queryset = Product.objects.all()
        data = ProductSerializer(queryset,many=True).data 
        return Response(data)

    if method == "POST":
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content') or None
        
            if content is None:
                content = title
            serializer.save(content=content)
       
            return Response(serializer.data)
        return Response({"invalid":"not good data"},status=400)