
from django.urls import path, include
from rest_framework import routers
from lct4.views import *

router = routers.SimpleRouter()
router.register(r'products', ProductsViewSet)
router.register(r'codes', CodesViewSet)
router.register(r'regions', RegionsViewSet)
router.register(r'districts', DistrictsViewSet)

urlpatterns = [
    path('registration/', Registration.as_view(), name='registration'),
    path('login/', LoginUser.as_view(), name='login'),
    path('profile/<slug:slug>', Profile.as_view(), name='profile'),
    path('', Main.as_view(), name='main'),
    path('products/', GetProducts.as_view(), name='products'),
    path('api/', include(router.urls))
]