from django import forms
from django.contrib.auth import get_user_model


class LoginUserForm(forms.Form):
    username = forms.ChoiceField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.ChoiceField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = get_user_model()
        fields = ['username', 'password']