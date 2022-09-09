from .views import *
from django.urls import path

urlpatterns = [
    path("everything", get_Everything),
    path('username=<username>', get_UserData),
    path('testheaders', headerTest)
]
