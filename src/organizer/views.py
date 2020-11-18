from .models import Tag, Startup, NewsLink
from .serializers import TagSerializer, StartupSerializer, NewsLinkSerializer
from django.shortcuts import get_object_or_404, render
from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView
from django.views.generic import ListView, DetailView
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_400_BAD_REQUEST
)


class TagList(ListView):

    queryset = Tag.objects.all()
    template_name = 'tag/list.html'


class TagDetail(DetailView):

    queryset = Tag.objects.all()
    template_name = 'tag/detail.html'


class StartupList(ListView):

    queryset = Startup.objects.all()
    template_name = 'startup/list.html'


class StartupDetail(DetailView):

    queryset = Startup.objects.all()
    template_name = 'startup/detail.html'


class TagApiDetail(RetrieveAPIView):

    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    lookup_field = "slug"

    def put(self, request, slug):
        tag = self.get_object(Tag)
        s_tag = self.serializer_class(
            tag,
            data=request.data,
            context={'request': request}
        )
        if s_tag.is_valid():
            s_tag.save()
            return Response(s_tag.data, HTTP_200_OK)
        return Response(s_tag.errors, HTTP_400_BAD_REQUEST)



class TagApiList(ListCreateAPIView):

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
