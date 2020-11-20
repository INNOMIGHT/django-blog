from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from .models import Tag, Startup, NewsLink


class TagSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"
        extra_kwargs = {
            "url": {
                "lookup_field": "slug",
                "view_name": "tag-api-detail",
            },
        }
        


class StartupSerializer(HyperlinkedModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = Startup
        fields = "__all__"
        extra_kwargs = {
            "url": {
                "lookup_field": "slug",
                "view_name": "startup-api-detail",
            }
        }

        def create(self, validated_data):
            tag_data_list = validated_data.pop("tags")
            startup = Startup.objects.create(**validated_data)
            tag_list = Tag.objects.bulk_create(
                [Tag(**tag_data) for tag_data in tag_data_list]
            )
            startup.tags.add(*tag_list)
            return startup


class NewsLinkSerializer(ModelSerializer):
    startup = StartupSerializer()

    class Meta:
        model = NewsLink
        fields = "__all__"
