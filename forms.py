# # داخل health/forms.py
# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
#
#
# class CustomSignupForm (UserCreationForm):
#     email = forms.EmailField ()
#
#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password1', 'password2')
#
#
# class LoginForm (forms.Form):
#     username = forms.CharField (max_length=150)
#     password = forms.CharField (widget=forms.PasswordInput ())
#
#
# class UploadFileForm (forms.Form):
#     file = forms.FileField ()

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# نموذج التسجيل (Custom Signup Form)
class CustomSignupForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


# نموذج تسجيل الدخول (Login Form)
class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput())


# نموذج رفع الملفات (Upload File Form)
class UploadFileForm(forms.Form):
    file = forms.FileField()
