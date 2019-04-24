from django.urls import path, include
import mysite.urls

urlpatterns = [
    path('', include(mysite.urls))
]
