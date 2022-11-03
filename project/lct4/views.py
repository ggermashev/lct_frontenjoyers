from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView
from lct4.forms import *


class Base:
    reg_menu = [
        {'title': 'sign up', 'url': 'registration'},
        {'title': 'log in', 'url': 'login'}
    ]
    main_menu = []

    def get_context(self, **kwargs):
        context = kwargs
        context['reg_menu'] = self.reg_menu
        return context

class Registration(CreateView):
    form_class = RegisterUserForm
    template_name = 'lct4/registration.html'
    success_url = '/login/'

    def form_valid(self, form):
        self.object = form.save()
        user = CustomUsers.objects.get(username=form.cleaned_data['username'])
        user.slug = form.cleaned_data['username']
        user.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'lct4/login.html'

    def get_success_url(self):
        return reverse_lazy('main')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class Profile(DetailView, Base):
    model = CustomUsers
    context_object_name = 'user'
    template_name = "lct4/profile.html"

    def get_object(self, queryset=None):
        slug = self.kwargs.get(self.slug_url_kwarg, None)
        print(CustomUsers.objects.get(slug=slug))
        return CustomUsers.objects.get(slug=slug)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context = dict(list(context.items()) + list(self.get_context().items()))
        return context

class Main(ListView, Base):
    model = CustomUsers
    template_name = 'lct4/main.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context = dict(list(context.items()) + list(self.get_context().items()))
        return context


class GetProducts(ListView, Base):
    model = Products
    template_name = 'lct4/products.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context = dict(list(context.items()) + list(self.get_context().items()))
        context['count'] = Products.objects.all().count()
        return context

