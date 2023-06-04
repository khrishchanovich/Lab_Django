from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm

from .forms import *
from .models import *
from .utils import *


# menu = [{'title': "Адреса компании", 'url_name': 'address'},
#         {'title': "Заключить договор", 'url_name': 'contract'},
#         {'title': "Оплата", 'url_name': 'pay'},
#         {'title': "Личный кабинет", 'url_name': 'login'}
#         ]


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


class CompanyAddress(ListView):
    model = InsuranceCompany
    template_name = 'mainapp/address.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Филиалы компании'
        context['let_selected'] = 0

        return context


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
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')
    raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Заключение договора о страховании')

        return dict(list(context.items()) + list(c_def.items()))


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


def pay(request):
    return HttpResponse("Как оплатить")


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

class LetCompany(ListView):
    model = InsuranceCompany
    template_name = 'mainapp/address.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Сортировка по алфавиту - ' + str(context['posts'][0].letter_id)
        context['let_selected'] = context['posts'][0].letter_id

        return context

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

class ShowAgent(ListView):
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
        context['menu'] = menu
        context['title'] = company.name
        context['company'] = company
        return context


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'mainapp/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self,*, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')

        return dict(list(context.items()) + list(c_def.items()))


class LoginUser(DataMixin, LoginView):
    form_class = AuthenticationForm
    template_name = 'mainapp/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Авторизация')

        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')