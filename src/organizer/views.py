from django.http import HttpResponse
from django.shortcuts import get_list_or_404, get_object_or_404
from django.views import View
import json
from .models import Tag


class TagApiDetail(View):

    def get(self, request, pk):
        tag = get_object_or_404(Tag, pk=pk)
        tag_json = json.dumps(
            dict(
                id=tag.pk,
                name=tag.name,
                slug=tag.slug,
            )
        )
        return HttpResponse(
            tag_json,
            content_type="application/json"
        )


class TagApiList(View):

    def get(self, request):
        tag_list = get_list_or_404(Tag)
        tag_json = json.dumps([
            dict(
                id=tags.pk,
                name=tags.name,
                slug=tags.slug,
            )
            for tags in tag_list
        ]
        )
        return HttpResponse(
            tag_json,
            content_type="application/json"
        )
