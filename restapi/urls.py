from django.urls import path

from restapi.views import lyrics

urlpatterns = [
    path("", lyrics, name='lyrics'),
]
