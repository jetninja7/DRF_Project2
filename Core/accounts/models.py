from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.
class MyAccountManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, email, password=None):
        if not email:
            raise ValueError('User must have an email address')
        if not username:
            raise ValueError('User must have an username')

        user = self.model(first_name=first_name, last_name=last_name, username=username)

    def create_superuser(self):
        pass


class Accounts(AbstractUser):
    first_name = models.CharField(max_length=50, null=False, default=None)
    last_name = models.CharField(max_length=50, null=True)
    username = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=100, unique=True)
    phone = models.CharField(max_length=15)


    #Required
    date_joined = models.DateTimeField(auto_now=True)
    last_login = models.DateTimeField(auto_now=True)
    is_active = models.DateTimeField(auto_now=False)
    is_staff = models.DateTimeField(auto_now=False)
    is_admin = models.DateTimeField(auto_now=False)
    is_superuser = models.DateTimeField(auto_now=False)
    is_anonymous = models.DateTimeField(auto_now=False)
    is_authenticated = models.DateTimeField(auto_now=False)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']


    def full_name(self):
        return f'{self.first_name} {self.last_name}'


    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True




