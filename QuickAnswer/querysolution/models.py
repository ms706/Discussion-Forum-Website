from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

class Category(models.Model):
	category=models.TextField()
	created_at = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.category

class Query(models.Model):
	user = models.ForeignKey(User,related_name="query",on_delete=models.CASCADE)
	category=models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
	query_title=models.CharField(max_length=100,blank=True)
	query_text=models.TextField()
	created_at = models.DateTimeField(default=timezone.now) 
	likes= models.ManyToManyField(User,blank=True,related_name="querylikes")
	dislikes= models.ManyToManyField(User,blank=True,related_name="querydislikes")

	class Meta:
		ordering = ['-created_at']
	def __str__(self):
		return str(self.user)+"-->"+str(self.query_title)

class Solution(models.Model) :
	query = models.ForeignKey(Query,related_name="solution",on_delete=models.CASCADE)
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	solution_text=models.TextField()
	created_at = models.DateTimeField(default=timezone.now)
	likes= models.ManyToManyField(User,blank=True,related_name="solutionlikes")
	dislikes= models.ManyToManyField(User,blank=True,related_name="solutiondislikes")
	
	class Meta:
		ordering = ['-created_at']

	def __str__(self):
		return str(self.query)+"-->"+str(self.solution_text)