from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class CustomUsers(User, models.Model):
    slug = models.SlugField(unique=True, null=True)

    def get_absolute_url(self):
        return reverse('profile', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Пользователи'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.first_name + self.last_name


class Products(models.Model):
    direction = models.CharField(max_length=32)
    date = models.CharField(max_length=16)
    country = models.CharField(max_length=64)
    product = models.CharField(max_length=32)
    ezdim = models.CharField(max_length=32, null=True)
    stoim = models.CharField(max_length=32,null=True)
    netto = models.CharField(max_length=32, null=True)
    kol = models.CharField(max_length=32, null=True)
    region = models.CharField(max_length=256)
    district = models.CharField(max_length=256)

    def get_absolute_url(self):
        return reverse('product', kwargs={'slug': self.product})

    class Meta:
        verbose_name = 'Продукты'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.product


class Codes(models.Model):
    description = models.CharField(max_length=256)

    def get_absolute_url(self):
        return reverse('code', kwargs={'code': self.code})

    class Meta:
        verbose_name = 'Коды'
        verbose_name_plural = 'Коды'

    def __str__(self):
        return self.description


class Regions(models.Model):
    name = models.CharField(max_length=128)

    def get_absolute_url(self):
        return reverse('region', kwargs={'id': self.id})

    class Meta:
        verbose_name = 'Регионы'
        verbose_name_plural = 'Регионы'

    def __str__(self):
        return self.name


class Districts(models.Model):
    name = models.CharField(max_length=128)

    def get_absolute_url(self):
        return reverse('district', kwargs={'id': self.id})

    class Meta:
        verbose_name = 'Округи'
        verbose_name_plural = 'Округи'

    def __str__(self):
        return self.name


class ProductNames(models.Model):
    code = models.IntegerField()
    description = models.CharField(max_length=256)

    def get_absolute_url(self):
        return reverse('code', kwargs={'code': self.code})

    class Meta:
        verbose_name = 'Коды2'
        verbose_name_plural = 'Коды2'

    def __str__(self):
        return self.description


class Nishas(models.Model):
    user_id = models.ForeignKey('CustomUsers', related_name='users', on_delete=models.CASCADE, null=True)
    region_id = models.ForeignKey('Regions', related_name='regions', on_delete=models.CASCADE, null=True)
    product_id = models.ForeignKey('Codes', related_name='products', on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'Нишы'
        verbose_name_plural = 'Нишы'

    def get_absolute_url(self):
        return reverse('nishas', kwargs={'user': self.user})

    def __str__(self):
        return self.product_id

