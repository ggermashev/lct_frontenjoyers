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
