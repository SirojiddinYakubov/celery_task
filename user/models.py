from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _
from user.managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    class Role(models.IntegerChoices):
        USER = 0, _('Пользователь')
        ADMIN = 1, _('Администратор')

    username = None

    email = models.EmailField(verbose_name=_('Электронная почта'), unique=True)
    last_name = models.CharField(verbose_name=_('Фамилия'), max_length=255, blank=True)
    first_name = models.CharField(verbose_name=_('Имя'), max_length=255, blank=True)
    middle_name = models.CharField(verbose_name=_('Отчество'), max_length=255, blank=True)
    role = models.IntegerField(verbose_name=_('Рол'), choices=Role.choices, default=Role.USER)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, auto_now=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return str(self.email)

    @property
    def fullname(self):
        return f"{self.last_name} {self.first_name} {self.middle_name}"

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"