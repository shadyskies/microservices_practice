from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django_channels.asgi import get_channel_layer


@login_required
def index(request):
    return render(request, 'chat/index.html')


def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })

def home(request):
    channel_layer = get_channel_layer()
    ch_group_list = channel_layer.groups('chat')
    return HttpResponse(f"<p>{ch_group_list}</p>")