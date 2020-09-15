from django import forms
from .models import *
from django.contrib.auth.hashers import check_password

class LoginForm(forms.Form):
    username=forms.CharField(
        error_messages={
            'required':'아아디를 입력하세요.'
        },
        max_length=64, label='ID'
    )
    password=forms.CharField(
        error_messages={
            'required':'비밀번호를 입력하세요'
        },
        widget=forms.PasswordInput, label='PW'
    )

    def clean(self):
        cleaned_data=super().clean()
        username=cleaned_data.get('username')
        password=cleaned_data.get('password')

        if username and password:
            myuser=Myuser.objects.get(username=username)
            if not check_password(password, myuser.password):
                self.add_error(u'password', '비밀번호 오류')
            else:
                self.user_id = myuser.id