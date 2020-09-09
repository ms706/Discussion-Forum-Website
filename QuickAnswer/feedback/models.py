from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserFeedback(models.Model):
	TYPE=(
			("","Select Feedback Type"),
			("Comment","Comment"),
			("Bug Report","Bug Report"),
			("Question","Question"),
		)
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	feedback_type=models.CharField(max_length=10,choices=TYPE,blank=False)
	feedback_content=models.TextField(null=True)
	

	def __str__(self):
		return '%s ----- %s ----- %s' % (self.user,self.feedback_type, self.feedback_content)	