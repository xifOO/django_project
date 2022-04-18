from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from permissions import IsSuperUserOrAuthor, IsSuperUserOrAuthorOrReadOnly, IsSuperUserOrReadOnly
from ..models import FootballPerson
from .serializers import *


class PersonAPIList(generics.ListAPIView):
    queryset = FootballPerson.objects.all()
    serializer_class = FootballPersonListSerializer
    permission_classes = [IsAuthenticated, IsSuperUserOrReadOnly]


class PersonAPICreate(generics.CreateAPIView):
    serializer_class = FootballPersonCreateSerializer
    permission_classes = [IsAuthenticated, IsSuperUserOrAuthorOrReadOnly]

    def get_queryset(self, serializer):
        query = FootballPerson.objects.create(serializer.data)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PersonAPIRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = FootballPerson.objects.all()
    serializer_class = FootballPersonUpdateDestroyRetrieveSerializer
    permission_classes = [IsAuthenticated, IsSuperUserOrAuthor]
