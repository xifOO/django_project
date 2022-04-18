from django.urls import path
from .views import *


urlpatterns = [
    path('', ClubAPIList.as_view(), name='club-list'),
    path('create/', ClubAPICreate.as_view(), name='club-create'),
    path('<int:pk>', ClubAPIDestroyUpdateRetrieve.as_view(), name='club-detail')
]