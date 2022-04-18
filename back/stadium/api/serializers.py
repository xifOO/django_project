from rest_framework import serializers
from ..models import Stadium


class StadiumListSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField(method_name='get_author')

    def get_author(self, obj):
        return obj.author.username

    class Meta:
        model = Stadium
        exclude = ['id']


class StadiumCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stadium
        exclude = ['author', 'id']


class StadiumRetrieveDestroyUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stadium
        exclude = ['id', 'author']