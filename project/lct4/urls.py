from django.urls import path
from lct4.views import *

urlpatterns = [
    path('registration/', Registration.as_view(), name='registration'),
    path('login/', LoginUser.as_view(), name='login'),
    path('profile/<slug:slug>', Profile.as_view(), name='profile'),
    path('', Main.as_view(), name='main'),
]