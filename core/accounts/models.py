from django.db import models

# Create your models here.
from django.db import models
from .managers import CustomUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import ugettext_lazy as _
import datetime
from django.conf import settings
from rest_framework.authtoken.models import Token
from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail 


# Create your models here.
USER_TYPES = (
    ("Admin", "Admin"),
    ("Doctor", "Doctor"),
    ("Patient", "Patient"),
)

class Department(models.Model):
    name = models.CharField(max_length=100)
    diagnostics = models.TextField()
    location = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(null=True, unique=True)
    name = models.CharField(max_length=50,null=True)
    user_type = models.CharField(max_length=30, choices=USER_TYPES, null=True,blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name = "All Users"
        verbose_name_plural = "All Users"

    def __str__(self):
        return f"{self.email}"    
    

class MultiToken(Token):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='auth_token',
            on_delete=models.CASCADE, verbose_name=_("User"))
     


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    email_plaintext_message = "{}?token={}".format(reverse('password_reset:reset-password-request'), reset_password_token.key)

    send_mail(
        # title:
        "Password Reset for {title}".format(title="Some website title"),
        # message:
        email_plaintext_message,
        # from:
        "info@nableinvent.com",
        # to:
        [reset_password_token.user.email]
    )