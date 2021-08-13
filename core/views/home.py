from django.shortcuts import redirect, render
from django.http import HttpResponse, request
from core.models import Product, Category
from django.views import View

# Create your views here.


def index(request):
    product = None
    category = Category.get_all_category()
    categoryID = request.GET.get('category')
    if categoryID:
        product = Product.get_all_products_by_category_id(categoryID)
    else:
        product = Product.get_all_products()
    data = {}
    data['product'] = product
    data['category'] = category
    return render(request, "index.html", data)


def property(request):
    return render(request, 'property.html')