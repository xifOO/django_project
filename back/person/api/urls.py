from django.urls import path
from .views import *


urlpatterns = [
    path('', PersonAPIList.as_view(), name='person-list'),
    path('create/', PersonAPICreate.as_view(), name='person-create'),
    path('<int:pk>', PersonAPIRetrieveUpdateDestroy.as_view(), name='person-detail')
]