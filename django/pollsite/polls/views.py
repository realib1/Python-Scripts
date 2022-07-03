from re import template
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.template import loader
from polls.models import Question

# Create your views here.

def index(request):
    latest_question = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question': latest_question,
    }
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', { 'question': question })

def results(request, question_id):
    response = 'You are looking at the results of question %s.'
    return HttpResponse(response % question_id)

def votes(request, question_id):
    return HttpResponse('You are voting on question %s.' % question_id)
    