from rest_framework.serializers import ModelSerializer
from .models import Post
from organizer.serializers import TagSerializer, StartupSerializer


class PostSerializer(ModelSerializer):

    tags = TagSerializer(many=True)
    startups = StartupSerializer(many=True)

    class Meta:
        model = Post
        fields = "__all"""





