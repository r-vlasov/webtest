from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
	title = models.TextField()
	text = models.TextField()
	added_at = models.DateTimeField(auto_now=True) 
	rating = models.IntegerField(default=0)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	likes = models.ManyToManyField(User, related_name='question_like_user')



class Answer(models.Model):
	text = models.TextField()
	added_at = models.DateTimeField(auto_now=True) 
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	author = models.ForeignKey(User, on_delete=models.CASCADE)

class QuestionManager(models.Manager):
	def new(self):
		return self.order_by('-added_ad')
	def popular(self):
		return self.order_by('-rating')
