from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', address, name='address'),
    path('addpage/', contract, name='contract'),
    path('contact/', pay, name='pay'),
    path('login/', login, name='login')
]