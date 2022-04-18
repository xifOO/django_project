from rest_framework import serializers
from ..models import FootballPerson


class FootballPersonListSerializer(serializers.ModelSerializer):
    rating = serializers.SerializerMethodField(method_name='get_rating')
    author = serializers.SerializerMethodField(method_name='get_author')
    club = serializers.SerializerMethodField(method_name='get_club')
    full_name = serializers.SerializerMethodField(method_name='get_full_name')

    def get_author(self, obj):
        return obj.author.username

    def get_rating(self, obj):
        return ((obj.pace + obj.shoots + obj.passing + obj.dribbling + obj.defending + obj.physics) // 6) + 10

    def get_club(self, obj):
        return obj.club.name

    def get_full_name(self, obj):
        return obj.first_name + ' ' + obj.second_name

    class Meta:
        model = FootballPerson
        exclude = ['id', 'first_name', 'second_name']


class FootballPersonCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FootballPerson
        exclude = ['id', 'author']


class FootballPersonUpdateDestroyRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = FootballPerson
        exclude = ['id', 'author']