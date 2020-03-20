from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager

from tinymce.models import HTMLField



class User(AbstractBaseUser, PermissionsMixin):
	email = models.EmailField(_('email address'), unique=True)
	is_staff = models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)
	date_joined = models.DateTimeField(auto_now_add=True)
	first_name = models.CharField(blank=True, max_length=50)
	last_name = models.CharField(blank=True, max_length=50)
	username = models.CharField(blank=True, unique=True, max_length=50)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []

	objects = CustomUserManager()

	def __str__(self):
		return self.email




class Post(models.Model):
	
	user = models.ForeignKey(User, on_delete=models.CASCADE, db_constraint=False, null=True, blank=True)
	text = HTMLField()
	updated_at = models.DateTimeField(auto_now=True)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.user)
