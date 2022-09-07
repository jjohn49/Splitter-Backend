from .views import get_Everything
from django.urls import path

urlpatterns = [
    path("", get_Everything),
]
