from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *

class UserReg(UserCreationForm):
	class Meta:
		model = User
		fields = ["first_name","last_name","email","username"]

class UserReg1(UserCreationForm):
	class Meta:
		model = User
		fields = ["first_name","last_name","email","username"]

class menuform(forms.ModelForm):
	class Meta:
		model = menu
		fields="__all__"

class custform(forms.ModelForm):
	class Meta:
		model = cust
		fields="__all__"

class custform1(forms.ModelForm):
	class Meta:
		model = cust1
		fields="__all__"