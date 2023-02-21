from rest_framework import serializers
from main.models import DefineUser,Post,follow,Like,Comment


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




