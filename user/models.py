from django.db import models
from django.contrib.auth.models import AbstractUser

from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager
)


# New User manager
class UserManager(BaseUserManager):
    def create_user(self, email, password=None, is_active=False, is_staff=False, is_admin=False, email_active=False):
        if not email:
            raise ValueError('Users must have an email address')
        if not password:
            raise ValueError('Users must have a password')
        userObject = self.model(
            email=self.normalize_email(email),
        )

        userObject.set_password(password)
        userObject.staff = is_staff
        userObject.admin = is_admin
        userObject.active = is_active
        userObject.confirm_email = email_active
        userObject.save(using=self._db)
        return userObject

    def create_staffuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
            is_staff=True
        )
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
            is_staff=True,
            is_admin=True
        )
        return user


# Create your models here.
# class User(AbstractUser):
#     name = models.CharField(max_length=255)
#     email = models.CharField(max_length=255, unique=True)
#     password = models.CharField(max_length=255)
#     username = None

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []

# Default User Models
class User(AbstractBaseUser):
    # User details
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    password = models.CharField(max_length=244)
    last_login = models.DateTimeField(
        blank=True, null=True, verbose_name='last login', auto_now=True)
    # Account details
    superuser = models.BooleanField(default=False)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    # Activation details
    active = models.BooleanField(default=True)
    confirm_email = models.BooleanField(default=False)
    confirm_email_date = models.DateTimeField(
        verbose_name='last login', auto_now=True)
    date_joined = models.DateTimeField(
        verbose_name='date joined', auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    # Get full name
    def get_full_name(self):
        return self.first_name + " "+self.last_name

    # Get short name
    def get_short_name(self):
        return self.last_name + " "

    # For checking permissions. to keep it simple all admin have ALL permissons
    def has_perm(self, perm, obj=None):
        return self.is_admin

    # Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active
