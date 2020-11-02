from django.urls import path
from .views import TagList, TagDetail


urlpatterns = [
    path("tag/<str:slug>/", TagDetail.as_view(), name="tag-detail"),
    path("tag/", TagList.as_view(), name="tag-list"),
]

