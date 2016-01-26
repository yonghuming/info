#coding=utf-8
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic

from .models import Poll, Choice, Question

class IndexView(generic.ListView):
	"""docstring for IndexView"""
	template_name = 'polls/index.html'
	context_object_name = 'polls_list'

	def get_queryset(self):
		"返回表单列表"
		return Poll.objects.all()

class DetailView(generic.DetailView):
	"""问卷详细页,django提供的对象操作api和强大
	基本上你只要提供了poll对象，那么关联的数据
	也就很自然的被取出来了
	通用细节视图绑定了pk，绑定了模型，然后剩下的
	就是自己的事情了
	"""
	model = Poll
	template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
	"""结果页"""
	model = Poll
	template_name = 'polls/detail.html'

def tijiao(request, poll_id):
	
	"""
	得到poll_id，request里有所有问题的答案
	把答案写到poll_id, choice_id, question_id
	"""
	return HttpResponse(request)