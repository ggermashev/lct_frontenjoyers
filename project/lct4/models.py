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

