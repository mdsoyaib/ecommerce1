from django.contrib import admin
from django.urls import path
from .views import index, login, signup

urlpatterns = [
    path('', index, name="homepage"),
    path('signup', signup),
    path('login', login),
]
