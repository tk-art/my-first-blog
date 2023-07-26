from channels.routing import ProtocolTypeRouter, URLRouter

from django.urls import path
from app.consumers import Consumer

websocket_urlpatterns = [
    path('chat/', Consumer.as_asgi()),
]