from django.shortcuts import render, redirect
from .models import Rooms, Message, Person
from django.http import HttpResponse, JsonResponse


# Create your views here.

def index(request):
    return render(request, 'index.html')


def login(request):
    room = request.POST['room']
    password = request.POST['password']
    if room.objects.filter(room, password).exists():
        return redirect('chatroom?')
    else:
        new_room = Rooms.objects.create(name=room)
        new_room.save()
    return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':
        room = request.POST['name']
        password = request.POST['password']
        confirmPassword = request.POST['confirmPassword']
        if password == confirmPassword:
            pass
    return render(request, 'signup.html')


def chatroom(request, room):
    username = request.POST.get('username')
    room_details = Rooms.objects.get(name=room)
    return render(request, 'chatroom.html', { 'username': username, 'room': room, 'room_details': room_details})


def send(request):
    message = request.POST['message']
    room = request.POST[' room']
    username = request.POST['username']
    room_id = request.POST[' room_id']

    new_message = Message.objects.create(value=message, user=username, room=room_id)
    return HttpResponse('message sent')


def getmessages(request, room):
    room_details = Rooms.objects.get(name=room)
    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({'messages': list(messages.values())})