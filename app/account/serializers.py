from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    password_2 = serializers.CharField(max_length=20, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'phone_number', 'password_2', 'profile_image']

    def validate(self, data):
        if data['password'] != data['password_2']:
            raise serializers.ValidationError('пароли должны совпадать')
        return data

    def create(self, validated_data):
        new_user = User(
            username=validated_data['username'],
            phone_number=validated_data['phone_number'],
            email=validated_data['email'],
            profile_image=validated_data['profile_image'],

        )
        new_user.set_password(validated_data['password'])
        new_user.save()
        return new_user
