from django.urls import path
from . import views

app_name="post"


urlpatterns=[
	path('create/', views.QueryCreateView.as_view(), name="querycreate"),
	path('<int:pk>/comment/',views.add_solution,name='add_solution'),
	path('myquery/', views.UserQueryList.as_view(), name="userquery"),
	path('mysolution/', views.UserSolutionList.as_view(), name="usersolution"),
	path('<int:pk>/edit/',views.QueryUpdateView.as_view(),name='query_edit'),
	path('<int:pk>/remove/',views.QueryDeleteView.as_view(),name='query_remove'),
	path('comment/<int:pk>/remove/',views.SolutionDeleteView.as_view(),name='solution_remove'),
	
]


