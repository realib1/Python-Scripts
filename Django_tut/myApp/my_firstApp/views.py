import re
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'index.html')


def counter(request):
    text = request.POST['text']
    number_of_words = len(text.split(' '))
    return render(request, 'counter.html', {'number_of_words': number_of_words})
