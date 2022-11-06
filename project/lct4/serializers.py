from rest_framework import serializers
from lct4.views import *
from lct4.models import *


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = "__all__"
        lookup_field = 'region'


class CodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Codes
        fields = "__all__"


class RegionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Regions
        fields = "__all__"


class DistrictsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Districts
        fields = "__all__"


class NishasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nishas
        fields = "__all__"


class ProductnamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductNames
        fields = "__all__"
