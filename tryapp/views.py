from django.shortcuts import render
from tryapp.models import * 
from rest_framework.decorators import api_view 


@api_view(['GET'])
def my_view(request):
    return render(request,template_name='home.html')

@api_view(['GET'])
def my_contact(request):
    return render(request,template_name='contact.html')

@api_view(['GET'])
def my_service(request):
    return render(request,template_name='service.html')