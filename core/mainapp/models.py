
from django.db import models
from mainapp.managers import CustomUserManager
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin
)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, )
    username = models.CharField(max_length=128, blank=True, )
    about = models.TextField(max_length=128, verbose_name='О себе', )
    is_staff = models.BooleanField(default=False, )
    is_active = models.BooleanField(default=False, )
    
    objects = CustomUserManager()
    
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
    
    def __str__(self):
        return f'{self.email}'

    USERNAME_FIELD = 'email'
    REQIRED_FIELDS = []
