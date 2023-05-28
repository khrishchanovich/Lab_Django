from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

from .models import *

menu = [{'title': "Адреса компании", 'url_name': 'address'},
        {'title': "Заключить договор", 'url_name': 'contract'},
        {'title': "Оплата", 'url_name': 'pay'},
        {'title': "Личный кабинет", 'url_name': 'login'}
]


def index(request):
    posts = InsuranceType.objects.all()
    cats = Category.objects.all()

    context = {
        'posts': posts,
        'cats': cats,
        'menu': menu,
        'title': 'Виды страхования',
        'cat_selected': 0
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


def show_info(request, post_id):
    return HttpResponse(f'Отображение информации о виде страхования с id = {post_id}')


def show_cat(request, cat_id):
    posts = InsuranceType.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()

    if len(posts) == 0:
        raise Http404()

    context = {
        'posts': posts,
        'cats': cats,
        'menu': menu,
        'title': 'Отображение по рубрикам',
        'cat_selected': cat_id
    }

    return render(request, 'mainapp/index.html', context=context)

