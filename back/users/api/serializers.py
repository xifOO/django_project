from rest_framework import serializers
from django.contrib.auth import get_user_model
from ..models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField()

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password', 'password2']

    def save(self, *args, **kwargs):
        user = User(
            email=self.validated_data['email'],
            username=self.validated_data['username']
        )
        password, password2 = self.validated_data['password'], self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({password: 'Passwords do not match'})

        user.set_password(password)
        user.save()
        return user

