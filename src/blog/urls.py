from django.urls import path
from .views import PostDetail, PostList


urlpatterns = [
    path("posts/<str:slug>/<int:year>/<int:month>", PostDetail.as_view(), name="post-detail"),
    path("posts/", PostList.as_view(), name="post-list")
]
