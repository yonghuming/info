#coding=utf-8
from django.db import models
from django.contrib import admin

from django.core.urlresolvers import reverse

class User(models.Model):
	username = models.CharField(max_length = 50)
	password = models.CharField(max_length = 50)

	def  __str__(self):
		return self.username

class UserAdmin(admin.ModelAdmin):
	list_display = ('username', 'password')
		

# Create your models here.
class QuestionSort(models.Model):
	questsort_text = models.CharField(max_length = 200)

	def __str__(self):
		return self.questsort_text

class Question(models.Model):
	'''
	1 单选
	2 多选
	3 填空
	4 判断
	5 简答
	添加不同类型的问题的实现
	新建问题的时候要可以选择问题的类型
	自定义新建问题类型界面
	
	'''
	QUESTION_TYPE_CHOICES = (
		('1','单选题'),
		('2','多选题'),
		('3','填空题'),
		('4','简答题'),
		)
	question_text = models.CharField(max_length = 200)
	pub_date = models.DateTimeField('date published')
	question_type = models.CharField(max_length = 200,default="1",choices = QUESTION_TYPE_CHOICES)

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

	def get_absolute_url(self):
		return reverse('poll-detail', kwargs={'pk':self.pk})
	def __str__(self):
		return self.poll_text

class UserPoll(models.Model):
	user_id = models.IntegerField()
	poll_id = models.CharField(max_length = 200)

	def add_poll(self,poll_id):
		self.poll_id += (',' + poll_id);

	def __str__(self):
		return str(self.user_id) +' & '+self.poll_id

class UserPollAnswer(models.Model):
	user_id = models.IntegerField()
	poll_id = models.IntegerField()
	questtion_id = models.IntegerField(default=1)
	choices = models.CharField(max_length = 200,blank = True)
	answer_text = models.CharField(max_length = 200,blank = True)