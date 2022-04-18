from django.urls import path, include


urlpatterns = [
    path('api/', include(('person.api.urls', 'api.person'), namespace='person-api')),
]