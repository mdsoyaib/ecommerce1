from django.shortcuts import redirect, render
from django.http import HttpResponse, request
from core.models.customer import Customer
from core.models.product import Product
from core.models.orders import Order
from django.contrib.auth.hashers import make_password, check_password
from django.views import View


class Checkout(View):
    def post(self, request):
        # print(request.POST)
        address = request.POST.get("address")
        phone = request.POST.get("phone")
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products = Product.get_products_by_id(list(cart.keys()))
        print(address, phone, customer, cart, products)

        for product in products:
            order = Order(customer=Customer(id=customer), product=product,
                        price = product.price, address=address, phone=phone,
                        quantity = cart.get(str(product.id)))

            order.save()
        request.session['cart'] = {}

        return redirect("cart")