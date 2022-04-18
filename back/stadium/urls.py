from django.urls import path, include


urlpatterns = [
    path('api/', include(('stadium.api.urls', 'stadium-api'), namespace='stadium-api'))
]