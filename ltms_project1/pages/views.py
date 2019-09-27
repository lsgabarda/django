from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView
from users.models import User

class HomePageView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'
    login_url = 'login'

class UserList(ListView):
    model = User
    template_name = 'user_list.html'

class PermissionList(TemplateView):
    template_engine = 'permission.html'