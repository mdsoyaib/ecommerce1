from django.shortcuts import redirect, render
from django.http import HttpResponse, request
from core.models.customer import Customer
from core.models.product import Product
from django.contrib.auth.hashers import make_password, check_password
from django.views import View



class Cart(View):
    def get(self, request):
        ids = print(list(request.session.get('cart').keys()))
        products = Product.get_products_by_id(ids)
        print(products)
        return render(request, 'cart.html')