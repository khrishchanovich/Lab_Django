from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('types/', types),
    path('branch/<slug:branchid>/', branch)
]