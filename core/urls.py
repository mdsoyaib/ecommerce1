from django.contrib import admin
from django.urls import path
from core.views.home import Index, property
from core.views.login import Login, logout
from .views.cart import Cart
from .views.signup import Signup
from .views.checkout import Checkout
from .views.orders import Orders

urlpatterns = [
    path('', Index.as_view(), name="homepage"),
    path('signup', Signup.as_view(), name="signup"),
    path('login', Login.as_view(), name="login"),
    path('logout', logout, name="logout"),
    path('cart', Cart.as_view(), name="cart"),
    path('checkout', Checkout.as_view(), name="checkout"),
    path('orders', Orders.as_view(), name="orders"),
    path('property', property),
]
