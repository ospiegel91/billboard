from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from .models import Message
import datetime


def index(request):
    session_id = True
    if request.POST.get('title') is not None:
        if session_id:
            msg_date = datetime.datetime.today()
            msg_title = request.POST.get('title')
            msg_content = request.POST.get('content')
            msg_author = request.POST.get('author')
            new_message = Message(title=msg_title, content=msg_content, author=msg_author, date=msg_date)
            new_message.save()

    msg_date = datetime.datetime.today().strftime('%d/%m/%Y')
    all_messages = Message.objects.all()
    context = {
        'today_date': msg_date,
        'all_msgs': all_messages,
    }
    return render(request, 'messageboard/index.html', context)

