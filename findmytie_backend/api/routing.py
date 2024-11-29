# api/routing.py
from django.urls import re_path

from .consumer import MyConsumer

path = re_path(r"ws/api/consumer", MyConsumer.as_asgi())
print(f"PATH: {path}")
websocket_urlpatterns = [
    path
]