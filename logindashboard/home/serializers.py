from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    # user_id = serializers.ReadOnlyField()

    class Meta:
        model = Post
        fields = '__all__'

    def create(self, validated_data):
        user = Post.objects.create(**validated_data)
        return user
