from django.db.models import Count
import requests

from .models import *

menu = [{'title': "Адреса компании", 'url_name': 'address'},
        {'title': "Заключить договор", 'url_name': 'contract'},
        {'title': "Оплата", 'url_name': 'pay'},
        {'title': "Существующие договоры", 'url_name': 'existing_contacts'},
        {'title': "Создать тип", 'url_name': 'read'},
        # {'title': 'Поиск', 'url_name': 'search'}
        {'title': "Мировые новости", 'url_name': 'news'},
        {'title': "Курс Биткоина", 'url_name': 'crypto'},
        ]


class DataMixin:
    paginate_by = 2

    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.annotate(Count('insurancetype'))
        lets = Letters.objects.annotate(Count('insurancecompany'))

        user_menu = menu.copy()


        """*******************************"""
        url_news = "https://newsapi.org/v2/top-headlines?country=us&apiKey=8c41bbbc22144f9ba156f765d9c0d67c"
        response_news = requests.get(url_news)
        data_news = response_news.json()
        articles = data_news["articles"]

        url_crypto = "https://rest.coinapi.io/v1/exchangerate/BTC/USD"
        headers = {"X-CoinAPI-Key": "6A9F2F49-2DE5-4763-A187-CBD7C4700939"}
        response_crypto = requests.get(url_crypto, headers=headers)
        data_crypto = response_crypto.json()
        rate = data_crypto["rate"]
        """*******************************"""

        if not self.request.user.is_authenticated:
            user_menu = menu.copy()
            user_menu.pop(1)
            user_menu.pop(1)
            user_menu.pop(1)
            user_menu.pop(1)
            user_menu.pop(1)
            user_menu.pop(1)

        if self.request.user.is_authenticated:
            user_menu = menu.copy()
            user_menu.pop(4)


        # if not self.request.user.is_superuser:
        #     user_menu = menu.copy()
        #     user_menu.pop(1)
        #     user_menu.pop(1)
        #     user_menu.pop(1)

        if self.request.user.is_staff:
            user_menu = menu.copy()
            user_menu.pop(0)
            user_menu.pop(0)
            user_menu.pop(0)
            user_menu.pop(0)
            user_menu.pop(1)
            user_menu.pop(1)


        context['menu'] = user_menu
        context['cats'] = cats
        context['lets'] = lets

        """*******************************"""
        context['rate'] = rate

        context['articles'] = articles
        """*******************************"""

        if 'cat_selected' not in context:
            context['cat_selected'] = 0

        if 'let_selected' not in context:
            context['let_selected'] = 0

        return context
