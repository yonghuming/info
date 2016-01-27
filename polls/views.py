from django.shortcuts import render,render_to_response,get_object_or_404
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import auth
from django import forms

from django.template import RequestContext, loader

from .models import Poll

def index(request):
	'''
	查看所有问卷
	'''
	polls_list = Poll.objects.all()
	template = loader.get_template('polls/index.html')
	context = RequestContext(request,{
		'polls_list': polls_list,
		})
	return HttpResponse(template.render(context))

def detail(request, poll_id):
	"""
	读取指定问卷的题目，同时涉及到多对多的写法
	"""
	poll = Poll.objects.get(pk = poll_id)
	questions_list = poll.questions.all()
	template = loader.get_template('polls/detail.html')
	context = RequestContext(request,{
		'questions_list': questions_list,
		'poll':poll,
		})
	return HttpResponse(template.render(context))


def results(request, poll_id):
	return HttpResponse('调查问卷填写结果 %s' % poll_id)

class UserForm(forms.Form):
	username = forms.CharField(label = '用户名',max_length = 200)
	password = forms.CharField(label = '密码',widget = forms.PasswordInput())


def login(request):
	if request.method == 'POST':
		userform = UserForm(request.POST)
		if userform.is_valid():

			username = userform.cleaned_data['username']
			password = userform.cleaned_data['password']

			user = auth.authenticate(username=username, password=password)

			if user is not None and user.is_active:
				auth.login(request,user)
				#returen view
				#return render_to_response('/polls',{'username':username})
				return HttpResponseRedirect('/polls/')
			else:
				#return view
				return HttpResponseRedirect('/polls/login/')
	else:
		#reuturn no valid
		userform = UserForm()
		
		template = loader.get_template('polls/login.html')
		context = RequestContext(request,{
			'userform': userform,
			})
		return HttpResponse(template.render(context))

# def login(request):

# 	userform = UserForm()
	
# 	template = loader.get_template('polls/index.html')
# 	context = RequestContext(request,{
# 		'userform': userform,
# 		})
# 	return HttpResponse(template.render(context))

		
	



