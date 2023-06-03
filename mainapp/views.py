from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404

from .forms import *
from .models import *

menu = [{'title': "Адреса компании", 'url_name': 'address'},
        {'title': "Заключить договор", 'url_name': 'contract'},
        {'title': "Оплата", 'url_name': 'pay'},
        {'title': "Личный кабинет", 'url_name': 'login'}
        ]


def index(request):
    posts = InsuranceType.objects.all()

    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Виды страхования',
        'cat_selected': 0
    }

    return render(request, 'mainapp/index.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def address(request):
    posts = InsuranceCompany.objects.all()

    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Филлиалы',
        'let_selected': 0
    }

    return render(request, 'mainapp/address.html', context=context)


def contract(request):
    if request.method == 'POST':
        form = ContractForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            try:
                Contract.objects.create(**form.cleaned_data)
                return redirect('home')
            except:
                form.add_error(None, 'Ошибка заключения контракта')
    else:
        form = ContractForm()

    return render(request, 'mainapp/contract.html', {'form': form, 'menu': menu, 'title': 'Заключение договора'})


def pay(request):
    return HttpResponse("Как оплатить")


def login(request):
    return HttpResponse("Авторизация")


def show_info(request, post_slug):
    post = get_object_or_404(InsuranceType, slug=post_slug)

    context = {
        'post': post,
        'menu': menu,
        'title': post.title,
        'cat_selected': post.cat_id,
    }

    return render(request, 'mainapp/post.html', context=context)


def show_cat(request, cat_slug):
    posts = InsuranceType.objects.filter(cat_id__slug=cat_slug)

    if len(posts) == 0:
        raise Http404()

    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Отображение по рубрикам',
        'cat_selected': cat_slug
    }

    return render(request, 'mainapp/index.html', context=context)


def show_let(request, let_slug):
    posts = InsuranceCompany.objects.filter(letter_id__slug=let_slug)

    if len(posts) == 0:
        raise Http404()

    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Отображение по буквам',
        'let_selected': let_slug
    }

    return render(request, 'mainapp/address.html', context=context)


def show_agent(request, agent_slug):
    company = get_object_or_404(InsuranceCompany, slug=agent_slug)

    agents = InsuranceAgent.objects.filter(address=company)

    context = {
        'agents': agents,
        'menu': menu,
        'company': company
    }

    return render(request, 'mainapp/agent.html', context=context)
