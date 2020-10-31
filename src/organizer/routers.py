from django.urls import path
from .views import TagApiDetail, TagApiList, StartupApiList, StartupApiDetail, NewsLinkApiDetail, NewsLinkApiList

urlpatterns = [
    path("tag/<str:slug>/", TagApiDetail.as_view(), name="tag-api-detail"),
    path("tag/", TagApiList.as_view(), name="tag-api-list"),
    path("startup/", StartupApiList.as_view(), name="startup-api-list"),
    path("startup/<str:slug>/", StartupApiDetail.as_view(), name="startup-api-detail"),
    path("newslink/<str:startup_slug>/<str:newslink_slug>/", NewsLinkApiDetail.as_view(), name="newslink-api-detail"),
    path("newslink/", NewsLinkApiList.as_view(), name="newslink_api_list"),
]
