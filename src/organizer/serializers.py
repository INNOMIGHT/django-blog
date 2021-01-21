from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer, SerializerMethodField
from .models import Tag, Startup, NewsLink
from rest_framework.reverse import reverse
from rest_framework.serializers import HyperlinkedRelatedField


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
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Startup
        fields = "__all__"
        extra_kwargs = {
            "url": {
                "lookup_field": "slug",
                "view_name": "startup-api-detail",
            }
        }


class NewsLinkSerializer(ModelSerializer):

    url = SerializerMethodField()
    startup = HyperlinkedRelatedField(
        queryset=Startup.objects.all(),
        lookup_field="slug",
        view_name="startup-api-detail",
    )

    class Meta:
        model = NewsLink
        exclude = ('id',)

    def get_url(self, newslink):

        return reverse(
            "newslink-api-detail",
            kwargs=dict(
                startup_slug=newslink.startup.slug,
                newslink_slug=newslink.slug
            ),
            request=self.context["request"],
        )
