from django.shortcuts import render,HttpResponse
from main.views import index

# Create your views here.

def index2(req):
    print(index(req))
    return HttpResponse("A")

