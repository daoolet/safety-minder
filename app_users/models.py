from django.db import models

from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_('The Email field must be set'))
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)
    

class CustomUser(AbstractUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)

    username = models.CharField(max_length=30, unique=False, blank=True, null=True)
    
    full_name = models.CharField(max_length=100, unique=True, blank=False, null=False)
    badge = models.PositiveIntegerField(unique=True, null=True)
    position = models.CharField(max_length=50, unique=False, blank=False, null=False)
    area = models.CharField(max_length=50, unique=False, blank=False, null=True)
    line_manager = models.CharField(max_length=100, unique=False, blank=False, null=True)

    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name = "Custom User"
        verbose_name_plural = "Custom Users"