#coding=utf-8
from django.shortcuts import render,render_to_response,get_object_or_404
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import auth
from django import forms
import urllib
from django.core.urlresolvers import reverse
from django.contrib.auth import logout

from django.template import RequestContext, loader

from .models import Poll,UserPoll,Question,UserPollAnswer
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy


class PollCreate(CreateView):
	model = Poll
	fields = ['id','poll_text']

@login_required
def index(request):
	'''
	查看所有问卷
	'''
	plist = []

	try:
		up = UserPoll.objects.get (pk = request.user.id)
		polls = up.poll_id.split(',')	
		for v in polls:
			plist.append(Poll.objects.get (pk = int(v)))
	finally:
	

		template = loader.get_template('polls/index.html')
		
		context = RequestContext(request,{
			'polls_list': plist,

			})
		return HttpResponse(template.render(context))


@login_required
def results(request, poll_id):
	poll = Poll.objects.get(pk = poll_id)
	questions_list = poll.questions.all()
	template = loader.get_template('polls/results.html')
	context = RequestContext(request,{
		'poll':poll,
		'questions_list': questions_list,
		})
	return HttpResponse(template.render(context))
	#return HttpResponse('调查问卷填写结果 %s' % poll_id)


@login_required
def detail(request, poll_id):
	"""
	读取指定问卷的题目，同时涉及到多对多的写法
	"""
	html = []
	if request.method == 'POST':
		#基础不熟悉，这个东西耗费了我两周的时间csrfmiddlewaretoken

		for obj in request.POST:
			if obj != 'csrfmiddlewaretoken':
				question_type = Question.objects.get(pk = int(obj[8:])).question_type

				if question_type == '1':
					html.append(obj+ '->' + request.POST[obj] + '\n')
					# insertAnswer(request.user.id, request.POST[obj])
					answer = UserPollAnswer()
					answer.user_id = request.user.id
					answer.poll_id = poll_id
					answer.question_id = int(obj[8:])
					answer.choices = request.POST[obj]
					if type(request.POST[obj]) == 'str':
						answer.choice_text = request.POST[obj]

					else:
						answer.choice_text = ''
						answer.choices = request.POST[obj]				
					answer.save()
				elif question_type == '2':

					answer = UserPollAnswer()
					answer.poll_id = poll_id
					answer.question_id = int(obj[8:])
					answer.choices = request.POST.getlist(obj).split(',')
					answer.save()
				else:
					nswer = UserPollAnswer()
					answer.poll_id = poll_id
					answer.question_id = int(obj[8:])
					answer.choice_text = request.POST[obj]
					answer.save()
					#html.append(request.POST.getlist('question8') )
							#html.append(question_type)
		#return HttpResponseRedirect('/polls/results')
		return HttpResponseRedirect(reverse('results', args=(poll_id,)))
		# return HttpResponse(template.render(request))
	else:

		poll = Poll.objects.get(pk = poll_id)
		questions_list = poll.questions.all()
		template = loader.get_template('polls/detail.html')
		context = RequestContext(request,{
			'questions_list': questions_list,
			'poll':poll,
			})
		return HttpResponse(template.render(context))
def insertAnswer(poll_id,choice_id,choice_text=None):
	

	pass





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


		
	



