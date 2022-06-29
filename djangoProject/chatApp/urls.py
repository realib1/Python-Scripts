from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('<str:chatroom>/', views.chatroom, name='chatroom'),
    path('/send', views.send, name='send'),
    path('getmessages/<str:room/', views.getmessages, name='getmessages')
]
