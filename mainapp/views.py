from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login
from django.core.exceptions import PermissionDenied

import requests

import json

from .forms import *
from .models import *
from .utils import *

menu = [{'title': "Создать тип", 'url_name': 'read'}
        ]


class TypeHome(DataMixin, ListView):
    model = InsuranceType
    template_name = 'mainapp/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Виды страхования')

        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return InsuranceType.objects.filter(is_published=True)


# def index(request):
#     posts = InsuranceType.objects.all()
#
#     context = {
#         'posts': posts,
#         'menu': menu,
#         'title': 'Виды страхования',
#         'cat_selected': 0
#     }
#
#     return render(request, 'mainapp/index.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


class CompanyAddress(DataMixin, ListView):
    model = InsuranceCompany
    template_name = 'mainapp/address.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Филиалы компании', let_selected=0)

        return dict(list(context.items()) + list(c_def.items()))


# def address(request):
#     posts = InsuranceCompany.objects.all()
#
#     context = {
#         'posts': posts,
#         'menu': menu,
#         'title': 'Филлиалы',
#         'let_selected': 0
#     }
#
#     return render(request, 'mainapp/address.html', context=context)
#

class AddContract(LoginRequiredMixin, DataMixin, CreateView):
    form_class = ContractForm
    template_name = 'mainapp/contract.html'
    success_url = reverse_lazy('pay')
    login_url = reverse_lazy('home')
    raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Заключение договора о страховании')

        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        form.instance.user = self.request.user

        return super().form_valid(form)


# def contract(request):
#     if request.method == 'POST':
#         form = ContractForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = ContractForm()
#
#     return render(request, 'mainapp/contract.html', {'form': form, 'menu': menu, 'title': 'Заключение договора'})


# def pay(request):
#     return HttpResponse("Как оплатить")

class Pay(DataMixin, ListView):
    model = InsuranceType
    template_name = 'mainapp/pay.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Оплата')

        return dict(list(context.items()) + list(c_def.items()))



# def login(request):
#     return HttpResponse("Авторизация")


# def show_info(request, post_slug):
#     post = get_object_or_404(InsuranceType, slug=post_slug)
#
#     context = {
#         'post': post,
#         'menu': menu,
#         'title': post.title,
#         'cat_selected': post.cat_id,
#     }
#
#     return render(request, 'mainapp/post.html', context=context)

class ShowInfo(DataMixin, DetailView):
    model = InsuranceType
    template_name = 'mainapp/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'])

        return dict(list(context.items()) + list(c_def.items()))


class TypeCat(DataMixin, ListView):
    model = InsuranceType
    template_name = 'mainapp/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Рубрика - ' + str(context['posts'][0].cat),
                                      cat_selected=context['posts'][0].cat_id)

        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self, *, object_list=None, **kwargs):
        return InsuranceType.objects.filter(cat__slug=self.kwargs['cat_slug'])


# def show_cat(request, cat_slug):
#     posts = InsuranceType.objects.filter(cat_id__slug=cat_slug)
#
#     if len(posts) == 0:
#         raise Http404()
#
#     context = {
#         'posts': posts,
#         'menu': menu,
#         'title': 'Отображение по рубрикам',
#         'cat_selected': cat_slug
#     }
#
#     return render(request, 'mainapp/index.html', context=context)


# def show_let(request, let_slug):
#     posts = InsuranceCompany.objects.filter(letter_id__slug=let_slug)
#
#     if len(posts) == 0:
#         raise Http404()
#
#     context = {
#         'posts': posts,
#         'menu': menu,
#         'title': 'Отображение по буквам',
#         'let_selected': let_slug
#     }
#
#     return render(request, 'mainapp/address.html', context=context)

class LetCompany(DataMixin, ListView):
    model = InsuranceCompany
    template_name = 'mainapp/address.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Сортировка по алфавиту - ' + str(context['posts'][0].letter_id),
                                      let_selected=context['posts'][0].letter_id)

        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self, *, object_list=None, **kwargs):
        return InsuranceCompany.objects.filter(letter_id__slug=self.kwargs['let_slug'])


# def show_agent(request, agent_slug):
#     company = get_object_or_404(InsuranceCompany, slug=agent_slug)
#
#     agents = InsuranceAgent.objects.filter(address=company)
#
#     context = {
#         'agents': agents,
#         'menu': menu,
#         'title': company.name,
#         'company': company
#     }
#
#     return render(request, 'mainapp/agent.html', context=context)
#


class ShowAgent(DataMixin, ListView):
    model = InsuranceAgent
    context_object_name = 'agents'
    template_name = 'mainapp/agent.html'

    def get_queryset(self):
        company = get_object_or_404(InsuranceCompany, slug=self.kwargs['agent_slug'])
        queryset = super().get_queryset()
        return queryset.filter(address=company)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        company = get_object_or_404(InsuranceCompany, slug=self.kwargs['agent_slug'])
        c_def = self.get_user_context(title=company.name)

        return dict(list(context.items()) + list(c_def.items()))


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'mainapp/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')

        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)

        return redirect('home')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'mainapp/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Авторизация')

        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)

    return redirect('login')


class ContractList(LoginRequiredMixin, DataMixin, ListView):
    model = Contract
    template_name = 'mainapp/contract_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Cписок ваших контрактов')

        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Contract.objects.filter(user=self.request.user)


class News(DataMixin, ListView):
    model = InsuranceType
    template_name = 'mainapp/news.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Мировые новости')

        return dict(list(context.items()) + list(c_def.items()))


class Crypto(DataMixin, ListView):
    model = InsuranceType
    template_name = 'mainapp/crypto.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Курс биткоина')

        return dict(list(context.items()) + list(c_def.items()))


def insurance_type_create(request):
    if not request.user.is_staff:
        raise PermissionDenied("Недостаточно прав.")

    if request.method == 'POST':
        form = InsuranceTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('read')
    else:
        form = InsuranceTypeForm()

        return render(request, 'mainapp/create.html', {'form': form, 'menu': menu})


def insurance_type_list(request):
    if not request.user.is_staff:
        raise PermissionDenied("Недостаточно прав.")

    ins_types = InsuranceType.objects.all()

    return render(request, 'mainapp/read.html', {'ins_types': ins_types, 'menu': menu})


def insurance_type_detail(request, id):
    if not request.user.is_staff:
        raise PermissionDenied("Недостаточно прав.")

    ins_types = get_object_or_404(InsuranceType, id=id)

    return render(request, 'mainapp/detail.html', {'ins_types': ins_types, 'menu': menu})


def insurance_type_update(request, id):
    if not request.user.is_staff:
        raise PermissionDenied("Недостаточно прав.")

    ins_type = get_object_or_404(InsuranceType, id=id)
    if request.method == 'POST':
        form = InsuranceTypeForm(request.POST, instance=ins_type)
        if form.is_valid():
            form.save()
            return redirect('detail', id=ins_type.id)
    else:
        form = InsuranceTypeForm(instance=ins_type)

        return render(request, 'mainapp/update.html', {'form': form, 'menu': menu})


def insurance_type_delete(request, id):
    if not request.user.is_staff:
        raise PermissionDenied("Недостаточно прав.")

    ins_type = get_object_or_404(InsuranceType, id=id)
    ins_type.delete()
    return redirect('read')


def search(request):
    query = request.GET.get('q')
    if query:
        types = InsuranceType.objects.filter(title__icontains=query)
    else:
        types = InsuranceType.objects.all()

    return render(request, 'mainapp/search.html', {'types': types})
