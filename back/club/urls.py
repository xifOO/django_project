from django.urls import path, include


urlpatterns = [
    path('api/', include(('club.api.urls', 'club-api'), namespace='club-api'))
]