from django.shortcuts import redirect, render
from django.http import HttpResponse, request
from core.models import Product, Category
from django.views import View


# Create your views here.


class Index(View):
    def post(self, request):
        product = request.POST.get('product')
        # print(product)
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:
                    cart[product] = quantity + 1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        print('cart', request.session['cart'])

        return redirect('homepage')

    def get(self, request):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
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
        # print('your are ', request.session.get('email'))
        return render(request, "index.html", data)


def property(request):
    return render(request, 'property.html')
