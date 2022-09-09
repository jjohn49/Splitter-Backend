from .views import *
from django.urls import path

urlpatterns = [
    path("get_everything", get_Everything),
    path('get_user<username>', get_UserData)
]
