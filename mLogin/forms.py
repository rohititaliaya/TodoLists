
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import*

class ulogin(forms.Form):
	Username = forms.CharField(max_length=100)
	Password = forms.CharField(widget=forms.PasswordInput,max_length=32)

class CreateUserForm(UserCreationForm):
	class Meta:
	      model=User
	      fields =['first_name','last_name','username','email','password1','password2']	

class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['Phonenumber']