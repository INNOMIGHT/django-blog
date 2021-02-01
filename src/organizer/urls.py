from django.urls import path
from .views import (
    TagList,
    TagDetail,
    StartupList,
    StartupDetail,
    TagDelete,
    TagCreate,
    TagUpdate
)


urlpatterns = [
    path("tag/create/", TagCreate.as_view(), name="tag-create"),
    path("tag/<str:slug>/", TagDetail.as_view(), name="tag-detail"),
    path("tag/", TagList.as_view(), name="tag-list"),

    path("tag/<str:slug>/update/", TagUpdate.as_view(), name="tag-update"),
    path("tag/<str:slug>/delete/", TagDelete.as_view(), name="tag-delete"),
    path("startup/", StartupList.as_view(), name="startup-list"),
    path("startup/<str:slug>", StartupDetail.as_view(), name="startup-detail"),
]

