from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
	title = models.TextField()
	text = models.CharField()
	added_at = models.DateTimeField(auth_now_add=True) 
	rating = models.IntegerField(default=0)
	author = models.ForeignKey(User)
	likes = models.ManyToManyField(User)
	objects = QuestionManager()



class Answer(models.Model):
	text = models.CharField()
	added_at = models.DateTimeField(auth_now_add=True) 
	question = models.ForeignKey(Question)
	author = models.ForeignKey(User)

class QuestionManager(models.Manager):
	def new(self):
		return self.order_by('-added_ad')
	def popular(self)
		return self.order_by('-rating')
