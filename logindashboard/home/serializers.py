from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    # recipients = serializers.ListField(
    #     child=serializers.CharField(allow_blank=False, trim_whitespace=False))
    # hashtags = serializers.ListField(
    #     child=serializers.CharField(allow_blank=False, trim_whitespace=False))

    class StringListField(serializers.ListField):
        recipients = serializers.CharField()
        hashtags = serializers.CharField()


    class Meta:
        fields = '__all__'
        model = Post

    def create(self, validated_data):
        user = Post.objects.create(**validated_data)
        return user
