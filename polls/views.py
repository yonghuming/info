#coding=utf-8
from django.shortcuts import render,render_to_response,get_object_or_404
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import auth
from django import forms

from django.contrib.auth import logout

from django.template import RequestContext, loader

from .models import Poll,UserPoll
@login_required
def index(request):
	'''
	查看所有问卷
	'''
	up = UserPoll.objects.get (pk = request.user.id)
	polls = up.poll_id.split(',')

	

	plist = []

	for v in polls:
		plist.append(Poll.objects.get (pk = int(v)))

	template = loader.get_template('polls/index.html')
	
	context = RequestContext(request,{
		'polls_list': plist,
		})
	return HttpResponse(template.render(context))

@login_required
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


@login_required
def results(request, poll_id):
	return HttpResponse('调查问卷填写结果 %s' % poll_id)



def login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST["password"]		

		user = auth.authenticate(username=username, password=password)

		if user is not None and user.is_active:
			auth.login(request,user)

			return HttpResponseRedirect('/polls/')
		else:

			return HttpResponseRedirect('/polls/login/')
	else:
		#return render_to_response('polls/login.html')
		polls_list = Poll.objects.all()
		template = loader.get_template('polls/login.html')
		context = RequestContext(request,{
			'polls_list': polls_list,
			})
		return HttpResponse(template.render(context))

def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/polls/')


		
	



