from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView, ListView, DetailView
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from lct4.forms import *
from lct4.serializers import *
from lct4.serializers import ProductsSerializer


class Base:
    reg_menu = [
        {'title': 'sign up', 'url': 'registration'},
        {'title': 'log in', 'url': 'login'}
    ]
    main_menu = [
        {'title': 'log out', 'url': 'logout'},
    ]

    def get_context(self, **kwargs):
        context = kwargs
        context['reg_menu'] = self.reg_menu
        context['main_menu'] = self.main_menu
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


def logout_user(request):
    logout(request)
    return redirect('main')


def dashboard(request):
    return render(request, 'lct4/dashboard.html')


class Profile(DetailView, Base):
    model = CustomUsers
    context_object_name = 'user'
    template_name = "lct4/profile.html"

    def get_object(self, queryset=None):
        pk = self.kwargs.get('id')
        return CustomUsers.objects.get(pk=pk)

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


class ProductRegionsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    lookup_field = 'region'

    def list(self):
        queryset = Products.objects.get(pk=1)
        serializer = ProductsSerializer(queryset)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        reg = kwargs.get('region')
        queryset = Products.objects.filter(region=reg).filter(direction='ИМ')
        serializer = ProductsSerializer(queryset, many=True)
        return Response(serializer.data)


class ProductCodesViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    lookup_field = 'code'

    def list(self):
        queryset = Products.objects.get(pk=1)
        serializer = ProductsSerializer(queryset)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        code = kwargs.get('code')
        code = code.rjust(2, '0')
        queryset = Products.objects.filter(product__startswith=code).filter(direction='ИМ')
        serializer = ProductsSerializer(queryset, many=True)
        return Response(serializer.data)


class ProductDistrictsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    lookup_field = 'district'

    def list(self):
        queryset = Products.objects.get(pk=1)
        serializer = ProductsSerializer(queryset)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        dist = kwargs.get('district')
        queryset = Products.objects.filter(district=dist).filter(direction='ИМ')
        serializer = ProductsSerializer(queryset, many=True)
        return Response(serializer.data)


class CodesViewSet(viewsets.ModelViewSet):
    queryset = Codes.objects.all()
    serializer_class = CodesSerializer


class RegionsViewSet(viewsets.ModelViewSet):
    queryset = Regions.objects.all()
    serializer_class = RegionsSerializer


class DistrictsViewSet(viewsets.ModelViewSet):
    queryset = Districts.objects.all()
    serializer_class = DistrictsSerializer


class NishasViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Nishas.objects.all()
    serializer_class = NishasSerializer
    lookup_field = 'user_id'

    def retrieve(self, request, *args, **kwargs):
        user_id = kwargs.get('user_id')
        queryset = Nishas.objects.filter(user_id=user_id)
        serializer = NishasSerializer(queryset, many=True)
        return Response(serializer.data)


class ProductNamesViewSet(viewsets.ModelViewSet):
    queryset = ProductNames.objects.all()
    serializer_class = ProductnamesSerializer
    lookup_field = 'code'

