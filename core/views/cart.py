from django.shortcuts import redirect, render
from django.http import HttpResponse, request
from core.models.customer import Customer
from django.contrib.auth.hashers import make_password, check_password
from django.views import View


class Cart(View):
    def get(self, request):
        return render(request, 'cart.html')