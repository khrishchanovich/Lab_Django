from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

from .models import *

menu = [{'title': "Адреса комании", 'url_name': 'address'},
        {'title': "Заключить договор", 'url_name': 'contract'},
        {'title': "Оплата", 'url_name': 'pay'},
        {'title': "Личный кабинет", 'url_name': 'login'}
]


def index(request):
    posts = InsuranceType.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Виды страхования'
    }

    return render(request, 'mainapp/index.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def address(request):
    return HttpResponse("Адреса комании")


def contract(request):
    return HttpResponse("Заключение контракта")


def pay(request):
    return HttpResponse("Как оплатить")


def login(request):
    return HttpResponse("Авторизация")

