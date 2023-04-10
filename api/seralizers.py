from rest_framework import serializers
from main.models import DefineUser,Post,follow,Like,Comment
from django.contrib.auth.models import User


class DefineUserSeralizer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='user.id')
    user = serializers.CharField(source='user.username')
    class Meta:
        model = DefineUser
        fields = '__all__'


class PostSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user

