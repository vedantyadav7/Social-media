from django.urls import reverse_lazy
from django.views.generic import CreateView
from . import forms
from django.contrib.auth import login, logout


class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("login")
    template_name = "account/signup.html" 


