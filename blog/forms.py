from django import forms
from django.db import models
from django.forms import fields
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email']

class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ['subject', 'content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 5}),
        }
        
class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Email", widget=forms.EmailInput(attrs={'class':'email-input'}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'id':'password-input'}))
    
    class Meta:
            model = User
            fields = ['username', 'password']

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('This user does not exist, please <a href="/sign up">register</a>')
            if not user.check_password(password):
                raise forms.ValidationError('You have entered the wrong password. <a href="#">Did you forget your password?</a>')
            if not user.is_active:
                raise forms.ValidationError('This account is not active. Please <a href="#">contact support</a>')
            return super(LoginForm, self).clean(*args, **kwargs)
