from django import forms
from django.utils import timezone
from .models import *


class ContractForm(forms.Form):
    last_name = forms.CharField(label='Ваша фамилия', max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-input'}))
    name = forms.CharField(label='Ваше имя', max_length=100, widget=forms.TextInput(attrs={'class': 'form-input'}))
    middle_name = forms.CharField(label='Ваше отчество', max_length=100,
                                  widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    phone_number = forms.CharField(label='Номер телефона', max_length=13)
    cat = forms.ModelMultipleChoiceField(queryset=InsuranceType.objects.all())
    address = forms.ModelMultipleChoiceField(queryset=InsuranceCompany.objects.all())
    accept_terms = forms.BooleanField(label='Я прочитал и согласен с условиями договора', required=True)
    initial_payment = forms.DecimalField(label='Первоначальный взнос')
