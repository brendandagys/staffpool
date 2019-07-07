from django.shortcuts import render
from django.utils.safestring import mark_safe
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.http import HttpResponse
from django.utils import timezone
import datetime

import json

from chat.models import Messages

# Create your views here.
# chat/views.py

def index(request):
    return render(request, 'chat/index.html', {})

# def room(request, room_name):
def room(request):

    # Get the last 10 messages and add to the context. Also, maybe import the staffpool models above?

    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps('group_chat'))
    })

def messages(request):

    if request.method == 'GET':

        last_10_messages_instance = Messages.objects.last()

        if last_10_messages_instance is None:
            message_1 = ''
            message_2 = ''
            message_3 = ''
            message_4 = ''
            message_5 = ''
            message_6 = ''
            message_7 = ''
            message_8 = ''
            message_9 = ''
            message_10 = ''

            author_1 = ''
            author_2 = ''
            author_3 = ''
            author_4 = ''
            author_5 = ''
            author_6 = ''
            author_7 = ''
            author_8 = ''
            author_9 = ''
            author_10 = ''

            timestamp = timezone.now() # Not sure if needed

            # timestamp is a datetime object!
            Messages.objects.create(author_1='', author_2='', author_3='', author_4='', author_5='', author_6='',
                                    author_7='', author_8='' , author_9='' , author_10='', message_1='', message_2='',
                                    message_3='', message_4='', message_5='', message_6='', message_7='', message_8='',
                                    message_9='', message_10='')#, timestamp = datetime.datetime.now())
            # new_messages_instance.save() # This should initiate the timestamp... I THINK IT SAVES ON CREATE

        else: # If there IS an instance of the Messages class...

            # print(datetime.datetime.now())
            # print(last_10_messages_instance.timestamp)

            reset_chats = 'No'
            # This line will clear all chats if the timestamp is a certain amount of time ago.
            # print((datetime.datetime.now() - last_10_messages_instance.timestamp).seconds)
            if ((datetime.datetime.now() - last_10_messages_instance.timestamp).seconds/60 > 120):
                reset_chats = 'Yes'

            print('Reset chats: ' + reset_chats)

            message_1 = last_10_messages_instance.message_1
            if message_1 is None or reset_chats == 'Yes':
                message_1 = ''
                last_10_messages_instance.message_1 = ''

            message_2 = last_10_messages_instance.message_2
            if message_2 is None or reset_chats == 'Yes':
                message_2 = ''
                last_10_messages_instance.message_2 = ''

            message_3 = last_10_messages_instance.message_3
            if message_3 is None or reset_chats == 'Yes':
                message_3 = ''
                last_10_messages_instance.message_3 = ''

            message_4 = last_10_messages_instance.message_4
            if message_4 is None or reset_chats == 'Yes':
                message_4 = ''
                last_10_messages_instance.message_4 = ''

            message_5 = last_10_messages_instance.message_5
            if message_5 is None or reset_chats == 'Yes':
                message_5 = ''
                last_10_messages_instance.message_5 = ''

            message_6 = last_10_messages_instance.message_6
            if message_6 is None or reset_chats == 'Yes':
                message_6 = ''
                last_10_messages_instance.message_6 = ''

            message_7 = last_10_messages_instance.message_7
            if message_7 is None or reset_chats == 'Yes':
                message_7 = ''
                last_10_messages_instance.message_7 = ''

            message_8 = last_10_messages_instance.message_8
            if message_8 is None or reset_chats == 'Yes':
                message_8 = ''
                last_10_messages_instance.message_8 = ''

            message_9 = last_10_messages_instance.message_9
            if message_9 is None or reset_chats == 'Yes':
                message_9 = ''
                last_10_messages_instance.message_9 = ''

            message_10 = last_10_messages_instance.message_10
            if message_10 is None or reset_chats == 'Yes':
                message_10 = ''
                last_10_messages_instance.message_10 = ''

            author_1 = last_10_messages_instance.author_1
            if author_1 is None or reset_chats == 'Yes':
                author_1 = ''
                last_10_messages_instance.author_1 = ''

            author_2 = last_10_messages_instance.author_2
            if author_2 is None or reset_chats == 'Yes':
                author_2 = ''
                last_10_messages_instance.author_2 = ''

            author_3 = last_10_messages_instance.author_3
            if author_3 is None or reset_chats == 'Yes':
                author_3 = ''
                last_10_messages_instance.author_3 = ''

            author_4 = last_10_messages_instance.author_4
            if author_4 is None or reset_chats == 'Yes':
                author_4 = ''
                last_10_messages_instance.author_4 = ''

            author_5 = last_10_messages_instance.author_5
            if author_5 is None or reset_chats == 'Yes':
                author_5 = ''
                last_10_messages_instance.author_5 = ''

            author_6 = last_10_messages_instance.author_6
            if author_6 is None or reset_chats == 'Yes':
                author_6 = ''
                last_10_messages_instance.author_6 = ''

            author_7 = last_10_messages_instance.author_7
            if author_7 is None or reset_chats == 'Yes':
                author_7 = ''
                last_10_messages_instance.author_7 = ''

            author_8 = last_10_messages_instance.author_8
            if author_8 is None or reset_chats == 'Yes':
                author_8 = ''
                last_10_messages_instance.author_8 = ''

            author_9 = last_10_messages_instance.author_9
            if author_9 is None or reset_chats == 'Yes':
                author_9 = ''
                last_10_messages_instance.author_9 = ''

            author_10 = last_10_messages_instance.author_10
            if author_10 is None or reset_chats == 'Yes':
                author_10 = ''
                last_10_messages_instance.author_10 = ''

            timestamp = last_10_messages_instance.timestamp

            if reset_chats == 'Yes':
                last_10_messages_instance.save()

        return JsonResponse({'message_1': message_1,
                             'message_2': message_2,
                             'message_3': message_3,
                             'message_4': message_4,
                             'message_5': message_5,
                             'message_6': message_6,
                             'message_7': message_7,
                             'message_8': message_8,
                             'message_9': message_9,
                             'message_10': message_10,
                             'author_1': author_1,
                             'author_2': author_2,
                             'author_3': author_3,
                             'author_4': author_4,
                             'author_5': author_5,
                             'author_6': author_6,
                             'author_7': author_7,
                             'author_8': author_8,
                             'author_9': author_9,
                             'author_10': author_10,

                             'timestamp': timestamp
                             })

    elif request.method == 'POST':

        last_10_messages_instance = Messages.objects.all()[0]

        # timestamp will be updated automatically
        last_10_messages_instance.message_10 = last_10_messages_instance.message_9
        last_10_messages_instance.message_9 = last_10_messages_instance.message_8
        last_10_messages_instance.message_8 = last_10_messages_instance.message_7
        last_10_messages_instance.message_7 = last_10_messages_instance.message_6
        last_10_messages_instance.message_6 = last_10_messages_instance.message_5
        last_10_messages_instance.message_5 = last_10_messages_instance.message_4
        last_10_messages_instance.message_4 = last_10_messages_instance.message_3
        last_10_messages_instance.message_3 = last_10_messages_instance.message_2
        last_10_messages_instance.message_2 = last_10_messages_instance.message_1

        last_10_messages_instance.message_1 = request.POST['message_1']

        last_10_messages_instance.author_10 = last_10_messages_instance.author_9
        last_10_messages_instance.author_9 = last_10_messages_instance.author_8
        last_10_messages_instance.author_8 = last_10_messages_instance.author_7
        last_10_messages_instance.author_7 = last_10_messages_instance.author_6
        last_10_messages_instance.author_6 = last_10_messages_instance.author_5
        last_10_messages_instance.author_5 = last_10_messages_instance.author_4
        last_10_messages_instance.author_4 = last_10_messages_instance.author_3
        last_10_messages_instance.author_3 = last_10_messages_instance.author_2
        last_10_messages_instance.author_2 = last_10_messages_instance.author_1

        last_10_messages_instance.author_1 = request.POST['author_1']

        last_10_messages_instance.timestamp = datetime.datetime.now()

        last_10_messages_instance.save()

        print(request.POST['message_1'])
        print(request.POST['author_1'])

        return HttpResponse()
