from rest_framework.viewsets import ModelViewSet
from .models import Tag, Startup
from .serializers import TagSerializer, StartupSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.status import HTTP_200_OK, HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST

class TagViewSet(ModelViewSet):

    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    lookup_field = "slug"


class StartupViewSet(ModelViewSet):

    queryset = Startup.objects.all()
    serializer_class = StartupSerializer
    lookup_field = "slug"

    @action(detail=True, methods=["GET", "HEAD", "POST")
    def tags(self, request, slug):
        startup = self.get_object()
        if request.methods in ("GET", "HEAD"):
            s_tag = TagSerializer(
                startup.tags,
                many=True,
                context={'request': request}
            )
            return Response(s_tag.data, status=HTTP_200_OK)
        tag_slug = request.data.get("slug")
        if not tag_slug:
            return Response(
                "Slug of tag must be specified",
                status=HTTP_400_BAD_REQUEST
            )
        tag = get_object_or_404(Tag, slug__iexact=tag_slug)
        startup.tags.add(tag)
        return Response(startup, status=HTTP_204_NO_CONTENT)