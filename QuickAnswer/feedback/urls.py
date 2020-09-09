from django.urls import path
from . import views

app_name="feedback"


urlpatterns=[
	path('', views.UserFeedback.as_view(), name="userfeedback"),
]