
from django.urls import path, include
from rest_framework import routers
from lct4.views import *

router = routers.SimpleRouter()
router.register('products/codes', ProductCodesViewSet)
router.register('products/regions', ProductRegionsViewSet)
router.register('products/districts', ProductDistrictsViewSet)
router.register('codes', CodesViewSet)
router.register('regions', RegionsViewSet)
router.register('districts', DistrictsViewSet)
router.register('nishas', NishasViewSet)
router.register('names', ProductNamesViewSet)

urlpatterns = [
    path('registration/', Registration.as_view(), name='registration'),
    path('login/', LoginUser.as_view(), name='login'),
    path('profile/<int:id>', Profile.as_view(), name='profile'),
    path('', Main.as_view(), name='main'),
    path('products/', GetProducts.as_view(), name='products'),
    path('api/', include(router.urls)),
    path('logout/', logout_user, name='logout'),
    path('dashboard/', dashboard, name='dashboard')
]

