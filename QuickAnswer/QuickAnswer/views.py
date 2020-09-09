from django.shortcuts import render,redirect,get_object_or_404
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import ListView,TemplateView,RedirectView
from querysolution.models import Query,Category,Solution
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from django.template.loader import render_to_string

class HomePage(ListView):
	model=Query
	template_name="index.html"
	paginate_by = 5
	
	def get_queryset(self):
		result = super(HomePage, self).get_queryset()
		result=Query.objects.order_by('-created_at')
		if self.request.GET.get("selected_category"):

			selected_category = self.request.GET.get('selected_category')
			result=Query.objects.order_by('-created_at')
			if selected_category == 'All' or selected_category == 'None':
				print("ALL")
				result=Query.objects.order_by('-created_at')
			else:
				print(selected_category)
				result = Query.objects.filter(category__category=selected_category).order_by('-created_at')		
		return result

	def get_context_data(self,**kwargs):
		context=super(HomePage,self).get_context_data(**kwargs)
		context['Query'] =Query.objects.all()
		context['Category']=Category.objects.all()
		#context['preference']=Preference.objects.all()
		context['input']=self.request.GET.get("selected_category")
		list_query = Query.objects.all().order_by('-created_at')
		#print(Query.objects.filter(querypreference__user=self.request.user).values('value'))
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


@login_required
def postPreferenceToggle(request,pk,preference):
	query=get_object_or_404(Query,id=pk)
	user=request.user
	if user.is_authenticated:
		if preference == 1:
			if user in query.likes.all():
				query.likes.remove(user)
			else:
				if user in query.dislikes.all():
					query.dislikes.remove(user)
				query.likes.add(user)
		elif preference == 2:
			print("2")
			if user in query.dislikes.all():
				query.dislikes.remove(user)
			else:
				if user in query.likes.all():
					query.likes.remove(user)
				query.dislikes.add(user)
				
	return redirect("home")

@login_required
def solutionPreferenceToggle(request,pk,preference):
	solution=get_object_or_404(Solution,id=pk)
	print(solution)
	user=request.user
	if user.is_authenticated:
		if preference == 1:
			if user in solution.likes.all():
				solution.likes.remove(user)
			else:
				if user in solution.dislikes.all():
					solution.dislikes.remove(user)
				solution.likes.add(user)
		elif preference == 2:
			print("2")
			if user in solution.dislikes.all():
				solution.dislikes.remove(user)
			else:
				if user in solution.likes.all():
					solution.likes.remove(user)
				solution.dislikes.add(user)
				
	return redirect("home")

 	
def autocomplete(request):
	if 'term' in request.GET:
		qs=Query.objects.filter(query_title__icontains=request.GET.get('term'))
		titles=list()
		for query in qs:
			titles.append(query.query_title)
		if len(titles)==0:
			titles.append("No Related Post Found")
		return JsonResponse(titles,safe=False)

def search(request):
	if request.method == 'GET': 
		searchtext = request.GET.get('searchtext')
		query=Query.objects.filter(query_title__icontains=request.GET.get('searchtext'))
		return render(request, 'index.html', {'page_obj': query,'searching':True})
	return render(request,'home')	