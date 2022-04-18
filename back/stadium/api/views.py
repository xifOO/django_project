from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from ..models import Stadium
from rest_framework.permissions import IsAuthenticated
from permissions import IsSuperUserOrAuthor, IsSuperUserOrAuthorOrReadOnly, IsSuperUserOrReadOnly


class StadiumAPIList(generics.ListAPIView):
    queryset = Stadium.objects.all()
    serializer_class = StadiumListSerializer
    permission_classes = [IsAuthenticated, IsSuperUserOrReadOnly]


class StadiumAPICreate(generics.CreateAPIView):
    serializer_class = StadiumCreateSerializer
    permission_classes = [IsAuthenticated, IsSuperUserOrAuthorOrReadOnly]

    def get_queryset(self, serializer):
        query = Stadium.objects.create(serializer.data)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class StadiumAPIDestroyUpdateRetrieve(generics.RetrieveUpdateDestroyAPIView):
    queryset = Stadium.objects.all()
    serializer_class = StadiumRetrieveDestroyUpdateSerializer
    permission_classes = [IsAuthenticated, IsSuperUserOrAuthor]
