from rest_framework import generics
from ..models import Club
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from permissions import IsSuperUserOrAuthor, IsSuperUserOrAuthorOrReadOnly, IsSuperUserOrReadOnly


class ClubAPIList(generics.ListAPIView):
    queryset = Club.objects.all()
    serializer_class = ClubListSerializer
    permission_classes = [IsAuthenticated, IsSuperUserOrReadOnly]


class ClubAPICreate(generics.CreateAPIView):
    serializer_class = ClubCreateSerializer
    permission_classes = [IsAuthenticated, IsSuperUserOrAuthorOrReadOnly]

    def get_queryset(self, serializer):
        query = Club.objects.create(serializer.data)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ClubAPIDestroyUpdateRetrieve(generics.RetrieveUpdateDestroyAPIView):
    queryset = Club.objects.all()
    serializer_class = ClubRetrieveDestroyUpdateSerializer
    permission_classes = [IsAuthenticated, IsSuperUserOrAuthor]



