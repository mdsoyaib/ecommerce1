from django.contrib import admin
from django.urls import path
from core.views.home import Index, property
from core.views.login import Login
from .views.signup import Signup

urlpatterns = [
    path('', Index.as_view(), name="homepage"),
    path('signup', Signup.as_view(), name="signup"),
    path('login', Login.as_view(), name="login"),
    path('property', property),
]
