from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('address/', address, name='address'),
    path('contract/', contract, name='contract'),
    path('pay/', pay, name='pay'),
    path('login/', login, name='login'),
    path('post/<int:post_id>/', show_info, name='post'),
    path('category/<int:cat_id>/', show_cat, name='category')
]