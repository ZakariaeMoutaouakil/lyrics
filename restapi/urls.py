from django.urls import path

from restapi.views import lyrics, test

urlpatterns = [
    path("test", test, name='test'),
    path("", lyrics, name='lyrics'),
]
