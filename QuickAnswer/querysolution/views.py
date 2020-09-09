from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView,UpdateView,DeleteView,ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from .forms import QueryCreateForm,SolutionForm
from .models import *


class QueryCreateView(LoginRequiredMixin,CreateView):
	model = Query
	login_url='/login/'
	redirect_field_name='index.html'
	form_class=QueryCreateForm
	success_url = reverse_lazy('home')

	def form_valid(self, form):
		if self.request.user.is_authenticated:
			form.instance.user = self.request.user
		return super(QueryCreateView, self).form_valid(form)
	
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

class UserQueryList(LoginRequiredMixin,ListView):
	template_name="index.html"
	paginate_by = 10
	def get_queryset(self):
		result= Query.objects.filter(user=self.request.user).order_by('-created_at')
		if self.request.GET.get("selected_category"):

			selected_category = self.request.GET.get('selected_category')
			result=Query.objects.order_by('-created_at')
			if selected_category == 'All' or selected_category == 'None':
				print("ALL")
				result=Query.objects.filter(user=self.request.user).order_by('-created_at')
			else:
				print(selected_category)
				result = Query.objects.filter(user=self.request.user,category__category=selected_category).order_by('-created_at')
		return result
	
	def get_context_data(self,**kwargs):
		context=super(UserQueryList,self).get_context_data(**kwargs)
		context['Query'] =Query.objects.filter(user=self.request.user)
		context['Category']=Category.objects.all()
		context['comment']=Solution.objects.all()
		context['userqueries']=True
		context['input']=self.request.GET.get("selected_category")
		list_query = Query.objects.all()
		paginator = Paginator(list_query, self.paginate_by)
		page = self.request.GET.get('page')
		try:
			file_query=paginator.page(page)
		except PageNotAnInteger:
			file_query=paginator.page(1)
		except EmptyPage:
			file_query=paginator.page(paginator.num_pages)
		context["list_query"]=file_query
		return context


class QueryUpdateView(LoginRequiredMixin,UpdateView):
	model=Query
	login_url='/login/'
	success_url = reverse_lazy('post:userquery')
	form_class=QueryCreateForm


class QueryDeleteView(LoginRequiredMixin,DeleteView):
	model =Query
	success_url = reverse_lazy('home')
	def get(self, request, *args, **kwargs):
		return self.post(request, *args, **kwargs)


class UserSolutionList(LoginRequiredMixin,ListView):
	template_name="index.html"
	paginate_by = 10
	def get_queryset(self):
		result= Query.objects.filter(solution__user=self.request.user).order_by('-created_at').distinct()
		if self.request.GET.get("selected_category"):

			selected_category = self.request.GET.get('selected_category')
			result=Query.objects.order_by('-created_at')
			if selected_category == 'All' or selected_category == 'None':
				print("ALL")
				result=Query.objects.filter(solution__user=self.request.user).order_by('-created_at').distinct()
			else:
				print(selected_category)
				result = Query.objects.filter(solution__user=self.request.user,category__category=selected_category).order_by('-created_at').distinct()
		return result
	
	def get_context_data(self,**kwargs):
		context=super(UserSolutionList,self).get_context_data(**kwargs)
		context['Category']=Category.objects.all()
		context['usersolution']=True
		context['input']=self.request.GET.get("selected_category")
		list_query = Query.objects.filter(solution__user=self.request.user).order_by('-created_at').distinct()
		paginator = Paginator(list_query, self.paginate_by)
		page = self.request.GET.get('page')
		try:
			file_query=paginator.page(page)
		except PageNotAnInteger:
			file_query=paginator.page(1)
		except EmptyPage:
			file_query=paginator.page(paginator.num_pages)
		context["list_query"]=file_query
		return context

class SolutionDeleteView(LoginRequiredMixin,DeleteView):
	model =Solution
	success_url = reverse_lazy('home')
	def get(self, request, *args, **kwargs):
		return self.post(request, *args, **kwargs)


@login_required
def add_solution(request,pk):
	query=get_object_or_404(Query,pk=pk)
	print(query)
	comment=Solution.objects.filter(query=query).order_by('created_at')
	if request.method=='POST':
		form=SolutionForm(request.POST)
		if form.is_valid():
			solution =form.save(commit=False)
			form.instance.user =request.user
			solution.query=query
			solution.save()
			return redirect(reverse_lazy('home'))
	else:
		form=SolutionForm()

	return render(request,'querysolution/solution_form.html',{'form':form,'comment':comment,'query':query})
