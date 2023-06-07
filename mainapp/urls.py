from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', TypeHome.as_view(), name='home'),
    path('address/', CompanyAddress.as_view(), name='address'),
    path('contract/', AddContract.as_view(), name='contract'),
    path('pay/', Pay.as_view(), name='pay'),
    path('login/', LoginUser.as_view(), name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('logout/', logout_user, name='logout'),
    path('post/<slug:post_slug>/', ShowInfo.as_view(), name='post'),
    path('category/<slug:cat_slug>/', TypeCat.as_view(), name='category'),
    path('letter/<slug:let_slug>/', LetCompany.as_view(), name='letter'),
    path('agent/<slug:agent_slug>/', ShowAgent.as_view(), name='agent'),
    path('contacts/', ContractList.as_view(), name='existing_contacts'),
    path('news/', News.as_view(), name='news'),
    path('crypto/', Crypto.as_view(), name='crypto'),
    path('read/', insurance_type_list, name='read'),
    path('detail/<int:id>/', insurance_type_detail, name='detail'),
    path('create/', insurance_type_create, name='create'),
    path('update/<int:id>/', insurance_type_update, name='update'),
    path('delete/<int:id>/', insurance_type_delete, name='delete'),
    # path('search/', search, name='search')

]
