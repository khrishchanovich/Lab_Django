from django import forms
from django.core.exceptions import ValidationError

from .models import *
import re


class ContractForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = 'Вид страхования не выбран'
        self.fields['ins_object'].empty_label = 'Объект страхования не выбран'
        self.fields['address'].empty_label = 'Филиал не выбран'

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        pattern = r'^\+375\d{9}$'
        if not re.match(pattern, phone_number):
            raise ValidationError('Номер телефона должен быть представлен в формате: +375*********')

        return phone_number

    def clean_initial_payment(self):
        initial_payment = self.cleaned_data['initial_payment']

        if initial_payment < 10:
            raise ValidationError('Первоначальный взнос должен быть больше 10 рублей')

        return initial_payment

    class Meta:
        model = Contract
        fields = '__all__'
