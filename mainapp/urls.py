from django.urls import path, re_path

from .views import *

urlpatterns = [
    # path('', index, name='home'),
    path('', TypeHome.as_view(), name='home'),
    # path('address/', address, name='address'),
    path('address/', CompanyAddress.as_view(), name='address'),
    # path('contract/', contract, name='contract'),
    path('contract/', AddContract.as_view(), name='contract'),
    path('pay/', pay, name='pay'),
    path('login/', LoginUser.as_view(), name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
    # path('post/<slug:post_slug>/', show_info, name='post'),
    path('post/<slug:post_slug>/', ShowInfo.as_view(), name='post'),
    # path('category/<slug:cat_slug>/', show_cat, name='category'),
    path('category/<slug:cat_slug>/', TypeCat.as_view(), name='category'),
    # path('letter/<slug:let_slug>/', show_let, name='letter'),
    path('letter/<slug:let_slug>/', LetCompany.as_view(), name='letter'),
    # path('agent/<slug:agent_slug>/', show_agent, name='agent'),
    path('agent/<slug:agent_slug>/', ShowAgent.as_view(), name='agent')
]
