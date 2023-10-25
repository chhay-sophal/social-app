from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Comment
from apps.user_authentication.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    profile_picture = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = ['profile_picture']

    def get_profile_picture(self, obj):
        return obj.get_profile_picture_url()
    

class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)
    class Meta:
        model = User
        fields = ['username', 'profile']


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'content', 'created_at', 'user']