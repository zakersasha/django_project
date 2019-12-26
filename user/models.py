from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    modified_at = models.DateTimeField(auto_now=True)

    email = models.EmailField(unique=True, verbose_name='Email address')

    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['-id']

    def __str__(self):
        return f'ID:{self.id} {self.email} {self.get_full_name()}'
