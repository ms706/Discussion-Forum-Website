from django import forms
from .models import Query,Category,Solution


class QueryCreateForm(forms.ModelForm):
	category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label='Choose category')
	class Meta:
		model = Query
		fields = ("query_title","query_text","category")
		widgets={
			'query_title':forms.Textarea(attrs={
								'class':'queryTitle',
								'placeholder':'Type Title Here',
								'rows':2}),
			'query_text':forms.Textarea(attrs={
								'class':'queryTextBox',
								'placeholder':'Describe Here'}),
		}
		
	def __init__(self,*args,**kwargs):
		super().__init__(*args,**kwargs)
		self.fields['category'].label='Category'
		self.fields['query_title'].label='Title'

class  SolutionForm(forms.ModelForm):
	class Meta:
		model = Solution
		fields=("solution_text",)
		widgets={
			'solution_text':forms.Textarea(attrs={
								'required': True,
                                'placeholder':"Type Your Comment Here",
                                'class':'queryTextBox'}), 
		}
		