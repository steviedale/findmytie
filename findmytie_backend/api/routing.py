# api/routing.py
from django.urls import re_path

from .consumers import GetListingsConsumer

path = re_path(r"ws/api/consumer", GetListingsConsumer.as_asgi())
print(f"PATH: {path}")
websocket_urlpatterns = [
    path
]