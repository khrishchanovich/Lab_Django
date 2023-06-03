from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('address/', address, name='address'),
    path('contract/', contract, name='contract'),
    path('pay/', pay, name='pay'),
    path('login/', login, name='login'),
    path('post/<slug:post_slug>/', show_info, name='post'),
    path('category/<slug:cat_slug>/', show_cat, name='category'),
    path('letter/<slug:let_slug>/', show_let, name='letter'),
    path('agent/<slug:agent_slug>/', show_agent, name='agent'),
]
