from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from .consumers import Consumer

application = ProtocolTypeRouter({
    'websocket': URLRouter([
        path('ws/chat/', Consumer.as_asgi()),
    ]),
})