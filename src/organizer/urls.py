from django.urls import path
from .views import TagList, TagDetail, StartupList, StartupDetail


urlpatterns = [
    path("tag/<str:slug>/", TagDetail.as_view(), name="tag-detail"),
    path("tag/", TagList.as_view(), name="tag-list"),
    path("startup/", StartupList.as_view(), name="startup-list"),
    path("startup/<str:slug>", StartupDetail.as_view(), name="startup-detail"),
]

