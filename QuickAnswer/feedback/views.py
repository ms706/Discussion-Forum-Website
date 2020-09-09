from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserFeedbackForm
from .models import UserFeedback

# Create your views here.

class UserFeedback(LoginRequiredMixin,CreateView):
	model = UserFeedback
	login_url='/login' 
	redirect_field_name='index.html'
	form_class=UserFeedbackForm
	success_url = reverse_lazy('home')

	def form_valid(self, form):
		if self.request.user.is_authenticated  :
			form.instance.user = self.request.user
		return super(UserFeedback, self).form_valid(form)
	
	def form_invalid(self, form):
		print(form.errors)
		return redirect(reverse_lazy('home'))

	def post(self, *args, **kwargs):
		form = self.get_form()
		self.object = None
		if form.is_valid():
			return self.form_valid(form)
		else:
			return self.form_invalid(form)