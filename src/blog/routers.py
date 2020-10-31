from django.urls import path
from .views import PostApiList, PostApiDetail


url_patterns = [
    path("posts/", PostApiList.as_view(), name="post-api-list"),
    path("posts/<str:slug>/<int:year>/<int:month>", PostApiDetail.as_view(), name="post-api-detail")
]