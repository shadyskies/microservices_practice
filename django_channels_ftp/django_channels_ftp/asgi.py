import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from channels.layers import get_channel_layer
import server.routing
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_channels_ftp.settings')

channel_layer = get_channel_layer()

application = ProtocolTypeRouter({
  "http": get_asgi_application(),
  "websocket": AuthMiddlewareStack(
        URLRouter(
            server.routing.websocket_urlpatterns
        )
    ),
})