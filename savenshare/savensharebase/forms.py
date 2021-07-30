from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import fields
from django.db.models.base import Model
from django.forms import widgets
from .models import LinkPost, LinkFile, LinkWritePost


class SignUpForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'joeschmoe', 'name': 'username'}))
    email = forms.CharField(widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'joeschmoe@xyz.com', 'name': 'email'}))
    password1 = forms.CharField(label='Enter password', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Type new password'}))
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Confirm password'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LinkPostForm(forms.ModelForm):
    class Meta:
        model = LinkPost
        fields = ('title', 'weblink')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Save\'nShare web link'}),
            'weblink': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'https://savenshare.com'})
        }


class LinkWritePostForm(forms.ModelForm):
    class Meta:
        model = LinkWritePost
        fields = ('posttitle', 'description')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'How to learn Dp effectively'}),
        }


class LinkFileForm(forms.ModelForm):
    class Meta:
        model = LinkFile
        fields = ('filetitle', 'uploadfile', )
