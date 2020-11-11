from django.urls import path, include
import mysite.urls
from pbx.urls import urlpatterns as ivr_urlpatterns

urlpatterns = [
    path('', include(mysite.urls)),
    path('ivr/', include(ivr_urlpatterns))

]
