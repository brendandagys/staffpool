from django.shortcuts import render
from django.utils.safestring import mark_safe
import json

# Create your views here.
# chat/views.py

def index(request):
    return render(request, 'chat/index.html', {})

def room(request, room_name):

    # Get the last 10 messages and add to the context. Also, maybe import the staffpool models above?

    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })
