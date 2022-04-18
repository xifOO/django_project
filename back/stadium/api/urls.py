from django.urls import path
from .views import *


urlpatterns = [
    path('', StadiumAPIList.as_view(), name='stadium-list'),
    path('create/', StadiumAPICreate.as_view(), name='stadium-create'),
    path('<int:pk>', StadiumAPIDestroyUpdateRetrieve.as_view(), name='stadium-detail')
]