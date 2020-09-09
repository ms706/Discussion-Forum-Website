from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class UserCreateForm(UserCreationForm):
	class Meta:
		fields=('username','email','password1','password2')
		model =get_user_model()
		widgets={
			"username": forms.TextInput(attrs={
										"placeholder":"Username"}),
			"email":forms.EmailInput(attrs={
								"placeholder":"Email Address"}),
			'password1':forms.PasswordInput(attrs={
								"placeholder":"Password"}),
			'password2':forms.PasswordInput(attrs={
								"placeholder":"Re-enter same Password"}), 
		}
