from django.urls import path
from core.views import RegisterAPIView


urlpatterns = [
    path('register', RegisterAPIView.as_view()),
]