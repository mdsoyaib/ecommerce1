from django.shortcuts import render
from django.views import View

from core.models import Product


class ProductDetails(View):
    def get(self, request, pk):
        product = Product.objects.get(id=pk)
        return render(request, 'details.html', {'product': product})