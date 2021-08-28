from django.contrib import admin
from django.urls import path
from core.views.home import Index, property
from core.views.login import Login, logout
from .views.signup import Signup

urlpatterns = [
    path('', Index.as_view(), name="homepage"),
    path('signup', Signup.as_view(), name="signup"),
    path('login', Login.as_view(), name="login"),
    path('logout', logout, name="logout"),
    path('property', property),
]
