from rest_framework import serializers

from posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    poster = serializers.ReadOnlyField(source='poster.username')
    poster_id = serializers.ReadOnlyField(source='poster.id')


    class Meta:
        model = Post
        fields = ['id', 'title', 'url', 'created', 'poster', 'poster_id',]