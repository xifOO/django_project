from django.urls import path
from .views import UserAPIRegistration


urlpatterns = [
    path('register', UserAPIRegistration.as_view(), name='register')
]