from .models import Tag, Startup, NewsLink
from .serializers import TagSerializer, StartupSerializer, NewsLinkSerializer
from django.shortcuts import get_object_or_404, render, redirect, reverse
from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView, RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_204_NO_CONTENT,
    HTTP_400_BAD_REQUEST
)
from django.views import View
from .forms import TagForm, StartupForm
from django.urls import reverse_lazy


class TagList(ListView):

    queryset = Tag.objects.all()
    template_name = 'tag/list.html'


class TagDetail(DetailView):

    queryset = Tag.objects.all()
    template_name = 'tag/detail.html'


class TagCreate(CreateView):

    form_class = TagForm
    model = Tag
    template_name = "tag/form.html"
    extra_context = {"update": False}


class TagUpdate(UpdateView):

    form_class = TagForm
    model = Tag
    template_name = "tag/form.html"
    extra_context = {"update": True}


class TagDelete(DeleteView):

    model = Tag
    template_name = "tag/confirm_delete.html"
    success_url = reverse_lazy('tag_list')


class StartupList(ListView):

    queryset = Startup.objects.all()
    template_name = 'startup/list.html'


class StartupDetail(DetailView):

    queryset = Startup.objects.all()
    template_name = 'startup/detail.html'


# class TagApiDetail(RetrieveUpdateDestroyAPIView):
#
#     queryset = Tag.objects.all()
#     serializer_class = TagSerializer
#     lookup_field = "slug"


# class TagApiList(ListCreateAPIView):
#
#     queryset = Tag.objects.all()
#     serializer_class = TagSerializer

#
# class StartupApiDetail(RetrieveAPIView):
#
#     queryset = Startup.objects.all()
#     serializer_class = StartupSerializer
#     lookup_field = "slug"
#
#
# class StartupApiList(ListAPIView):
#
#     queryset = Startup.objects.all()
#     serializer_class = StartupSerializer

#
# class NewsLinkApiDetail(RetrieveAPIView):
#
#     queryset = NewsLink.objects.all()
#     serializer_class = NewsLinkSerializer
#
#     def get_object(self):
#         startup_slug = self.kwargs.get("startup_slug")
#         newslink_slug = self.kwargs.get("newslink_slug")
#         queryset = self.filter_queryset(self.get_queryset())
#
#         newslink = get_object_or_404(
#             queryset,
#             slug=newslink_slug,
#             startup__slug=startup_slug
#         )
#         self.check_object_permissions(
#             self.request, newslink
#         )
#         return newslink
#
#
# class NewsLinkApiList(ListAPIView):
#
#     queryset = NewsLink.objects.all()
#     serializer_class = NewsLinkSerializer
