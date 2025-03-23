from django.http import HttpResponse
from django.shortcuts import render

# from main.content import products
from main.models import Countries, Products

countries = Countries.objects.all()
products = Products.objects.all()
# products.sort(key=lambda x: x["price"])
context = {"products": products, "countries": countries}


# Create your views here.
def index(request):
    return HttpResponse(render(request, "main/index.html", context))
