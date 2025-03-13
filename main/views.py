from django.http import HttpResponse
from django.shortcuts import render
from main.content import products

products.sort(key=lambda x: x["price"])
context = {"products": products}


# Create your views here.
def index(request):
    return HttpResponse(render(request, "main/index.html", context))
