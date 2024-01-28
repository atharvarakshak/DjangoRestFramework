import json
from django.shortcuts import render
from products.models import Product

from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

from products.serializers import ProductSerializer

# from django.http import JsonResponse,HttpResponse


@api_view(["POST"])
def api_home(request,*args,**kwargs):
    '''
        drf api view due to @api_view
    '''
    # if request.method != "POST":
    #     return Response({"detail":"GET not allowed"},status=405)

    data  = request.data
    
    # instance = Product.objects.all().order_by("?").first()
    # data={}
    # if instance:
    #     # data['id']=model_data.id
    #     # data['title']=model_data.title
    #     # data['content']=model_data.content
    #     # data['price']=model_data.price
        
    #     # data = model_to_dict(instance,fields=['id','title','price','sale_price'])
    #     data = ProductSerializer(instance).data
    return Response(data)

        # model instance (model_data)
        # turn a python dict
        # return json to my client
        # json_data_str = json.dumps(data)









# def api_home(request,*args,**kwargs):
#     # request -> HTTP req -> Django  not by python requests
#     print(request.GET)
#     print(request.POST)
#     body = request.body  #byte satring of json data
#     data ={}
#     try:
#         data = json.load(body) #takes in json data and turns it into python dict
#     except:
#         pass

#     print(data)
#     data['params']=dict(request.GET)
#     data['headers']=dict(request.headers)
#     data['content_type']=request.content_type

#     return JsonResponse(data)