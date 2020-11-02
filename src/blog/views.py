from rest_framework.generics import ListAPIView, RetrieveAPIView
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, View
from .serializers import PostSerializer
from .models import Post


class PostList(ListView):

    queryset = Post.objects.all()
    template_name = 'blog/list.html'


class PostDetail(View):

    def get(self, request, year, month, slug):
        post = get_object_or_404(
            Post,
            slug=slug,
            pub_date__year = year,
            pub_date__month=month
        )
        return render(request, 'blog/detail.html', {"post": post})


class PostApiList(ListAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostApiDetail(RetrieveAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_object(self):
        year = self.kwargs.get("year")
        month = self.kwargs.get("month")
        slug = self.kwargs.get("slug")

        queryset = self.filter_queryset(self.get_queryset())

        post = get_object_or_404(
            queryset,
            pub_date__year=year,
            pub_date__month=month,
            slug=slug,
        )
        self.check_object_permissions(self.request, post)
        return post

