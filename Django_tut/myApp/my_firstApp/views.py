from django.shortcuts import render
from .models import Feature
# Create your views here.

def index(request):
    feature = Feature()
    feature.name = "?"
    feature.details = "Type in any amount of worlds and submit for a count, it will show you the amount of words right after submission."
    feature.is_true = False
    
    return render(request, 'index.html', {'feature1': feature})


def counter(request):
    text = request.POST['text']
    number_of_words = len(text.split(' '))
    return render(request, 'counter.html', {'number_of_words': number_of_words})
