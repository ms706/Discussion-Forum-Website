from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserFeedback


class UserFeedbackForm(forms.ModelForm):
	class Meta:
		fields=("feedback_type","feedback_content")
		model =UserFeedback
		widgets={
			"feedback_type": forms.Select(attrs={
								'class':'feedbacktypebox'}),
			'feedback_content':forms.Textarea(attrs={
								'required': True,
                                'placeholder':"Enter Your Feedback Here",
                                'class':'feedbackcontentbox'}), 
		}

	def __init__(self,*args,**kwargs):
		super().__init__(*args,**kwargs)
		self.fields['feedback_type'].label='Feedback Type'
		self.fields['feedback_content'].label='Describe Feedback'