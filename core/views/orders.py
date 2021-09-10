from django.shortcuts import redirect, render
from django.http import HttpResponse, request
from core.models.customer import Customer
from core.models.product import Product
from core.models.orders import Order
from django.contrib.auth.hashers import make_password, check_password
from django.views import View
from core.middlewares.auth import auth_middleware
from django.utils.decorators import method_decorator


class Orders(View):

    # @method_decorator(auth_middleware)

    def get(self, request):
        customer = request.session.get('customer')
        orders = Order.get_orders_by_customer(customer)
        # print(orders)
        return render(request, 'orders.html', {'orders': orders})