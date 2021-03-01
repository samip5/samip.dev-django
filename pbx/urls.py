from django.urls import path, include
from .views import welcome, test

urlpatterns = [
    path('', welcome),
    path('test/', test),
]
