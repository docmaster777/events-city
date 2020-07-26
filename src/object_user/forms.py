from django import forms
from .models import *
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

class ObjectUserCreateForm(forms.ModelForm):
    title = forms.CharField(max_length=255, required=True)
    category = forms.CharField(max_length=255, required=True)
    site = forms.CharField(max_length=255, required=False)
    address = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '2'}), required=False,
                              label='адрес')
    phone = forms.CharField(max_length=16, required=True, validators=[
        RegexValidator(
            regex='^([0-9\(\)\/\+ \-]*)$',
            message='не верный формат телефона',
            code='invalid_phone'
        ),
    ])
    information = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '2'}), required=False,
                              label='Информация')
    working_hours = forms.CharField(max_length=255, required=False, label='Время работы')
    city_u = forms.CharField(required=True)
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '2'}), required=False,
                                  label='Описание')
    email = forms.EmailField(required=True)

    class Meta:
        model = ObjectUser
        fields = ('title', 'category', 'site', 'address', 'phone', 'information', 'working_hours', 'city_u', 'description', 'email',)