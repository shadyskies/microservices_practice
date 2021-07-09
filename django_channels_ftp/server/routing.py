from django.urls import path
from server import consumers

websocket_urlpatterns = [
    path('ws/ftp/', consumers.ChatConsumer.as_asgi()),
]