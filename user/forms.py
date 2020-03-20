from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import User, Post


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = User
        fields = ('email', 'groups',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('email', 'groups', )



class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('email', 'username', 'password', 'first_name', 'last_name')

class PostForm(forms.ModelForm):
    class Meta():
        model = Post
        fields = ('text', )