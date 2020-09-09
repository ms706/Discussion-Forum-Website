from django import forms
from .models import *


class UserProfileForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model =  UserProfile
        fields = ('picture','about')

        widgets={
			'about':forms.Textarea(attrs={
								'placeholder':'Type Something About You',
								'rows':3}),
		}