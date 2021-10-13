from django.urls import path, include
from .views import send

urlpatterns = [
    path('send/', send),
]
