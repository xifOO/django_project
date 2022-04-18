from rest_framework import serializers
from ..models import Club, Stadium


class ClubListSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField(method_name='get_author')
    stadium = serializers.SerializerMethodField(method_name='get_stadium')

    def get_author(self, obj):
        return obj.author.username

    def get_stadium(self, obj):
        return obj.stadium.name

    class Meta:
        model = Club
        exclude = ['id']


class ClubCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        exclude = ['author', 'id']


class ClubRetrieveDestroyUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        exclude = ['id', 'author']
