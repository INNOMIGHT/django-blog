from django.http import HttpResponse
from django.shortcuts import get_list_or_404, get_object_or_404
from .models import Tag
from .serializers import TagSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class TagApiDetail(APIView):

    def get(self, request, pk):
        tag = get_object_or_404(Tag, pk=pk)
        s_tag = TagSerializer(tag)
        return Response(s_tag.data)


class TagApiList(APIView):

    def get(self, request):
        tag_list = get_list_or_404(Tag)
        s_tag = TagSerializer(tag_list, many=True)
        return Response(s_tag.data)
