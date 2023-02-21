from rest_framework import serializers
from main.models import DefineUser,Post,follow,Like,Comment


class DefineUserSeralizer(serializers.ModelSerializer):
    class Meta:
        model = DefineUser
        fields = '__all__'


class PostSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'




