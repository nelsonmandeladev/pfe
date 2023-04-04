from django.db import models

import uuid
from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUSerManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_('The User Email should be provided'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('role', "Directeur")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True'))

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True'))

        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    username = None
    first_name = phone = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )
    last_name = phone = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )
    email = models.CharField(
        _('Email'),
        max_length=255,
        unique=True,
        null=True,
        blank=True
    )
    phone = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )
    address = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )
    zip_code = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )
    region = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )
    town = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )
    ROLES = (
        ("Personel", "Personel"),
        ("DAF", "DAF"),
        ("Directeur", "Directeur"),
    )
    role = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        choices=ROLES,
        default="Personel"
    )
    as_deleted = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    two_factor_auth = models.BooleanField(default=False)
    date_joined = models.DateTimeField(
        _('Date'), auto_now_add=True, null=True, blank=True)
    last_update = models.DateTimeField(
        _('LastUpdate'), auto_now=True, null=True, blank=True)

    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'

    objects = CustomUSerManager()

    class Meta:
        verbose_name = 'User account'
        verbose_name_plural = 'User account'

    def __str__(self):
        return self.email
