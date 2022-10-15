from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView, LogoutView
from . import models
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import LoginForm, SignUpForm


class TeamList(ListView):
    template_name = "list.html"
    model = models.TeamModel

class TeamDetail(LoginRequiredMixin, DetailView):
    login_url = reverse_lazy("login")

    template_name = "detail.html"
    model = models.TeamModel

class Login(LoginView):
    template_name = "login.html"
    form_class = LoginForm
    success_url = reverse_lazy("list")


class Logout(LogoutView):
    template_name = "logout.html"

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

