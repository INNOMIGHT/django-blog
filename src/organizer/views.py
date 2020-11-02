from .models import Tag, Startup, NewsLink
from .serializers import TagSerializer, StartupSerializer, NewsLinkSerializer
from django.shortcuts import get_object_or_404, render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from django.views import View


class TagList(View):

    def get(self, request):
        tag_list = Tag.objects.all()
        context = {"tag_list": tag_list}
        return render(request, 'tag/list.html', context)


class TagDetail(View):
    def get(self, request, slug):
        tag = get_object_or_404(Tag, slug=slug)
        context = {'tag': tag}
        return render(request, 'tag/detail.html', context)



class TagApiDetail(RetrieveAPIView):

    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    lookup_field = "slug"


class TagApiList(ListAPIView):

    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class StartupApiDetail(RetrieveAPIView):

    queryset = Startup.objects.all()
    serializer_class = StartupSerializer
    lookup_field = "slug"


class StartupApiList(ListAPIView):

    queryset = Startup.objects.all()
    serializer_class = StartupSerializer


class NewsLinkApiDetail(RetrieveAPIView):

    queryset = NewsLink.objects.all()
    serializer_class = NewsLinkSerializer

    def get_object(self):
        startup_slug = self.kwargs.get("startup_slug")
        newslink_slug = self.kwargs.get("newslink_slug")
        queryset = self.filter_queryset(self.get_queryset())

        newslink = get_object_or_404(
            queryset,
            slug=newslink_slug,
            startup__slug=startup_slug
        )
        self.check_object_permissions(
            self.request, newslink
        )
        return newslink


class NewsLinkApiList(ListAPIView):

    queryset = NewsLink.objects.all()
    serializer_class = NewsLinkSerializer
