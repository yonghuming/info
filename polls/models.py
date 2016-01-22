from django.db import models

# Create your models here.


class Question(models.Model):
	question_text = models.CharField(max_length = 200)
	pub_date = models.DateTimeField('date published')

	def __str__(self):
		return self.question_text

class Choice(models.Model):
	question = models.ForeignKey(Question)
	choice_text = models.CharField(max_length = 200)
	votes = models.IntegerField(default = 0)

	def __str__(self):
		return self.choice_text

class Poll(models.Model):
	"""
	问卷类，实际的问题
	"""
	poll_text = models.CharField(max_length = 200)
	questions = models.ManyToManyField(Question)

	def __str__(self):
		return self.poll_text