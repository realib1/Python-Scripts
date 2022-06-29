from django.contrib import admin
from .models import Rooms, Message, Person

# Register your models here.

admin.site.register(Rooms)
admin.register(Message)
admin.site.register(Person)
