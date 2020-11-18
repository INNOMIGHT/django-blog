from django.urls import path
from .views import TagApiDetail, TagApiList, StartupApiList, StartupApiDetail, NewsLinkApiDetail, NewsLinkApiList
from rest_framework.routers import SimpleRouter
from .viewsets import TagViewSet

api_router = SimpleRouter()
api_router.register("tag", TagViewSet, base_name="api-tag")
api_routes = api_router.urls

urlpatterns = api_routes + [
    path("tag/<str:slug>/", TagApiDetail.as_view(), name="tag-api-detail"),
    path("tag/", TagApiList.as_view(), name="tag-api-list"),
    path("startup/", StartupApiList.as_view(), name="startup-api-list"),
    path("startup/<str:slug>/", StartupApiDetail.as_view(), name="startup-api-detail"),
    path("newslink/<str:startup_slug>/<str:newslink_slug>/", NewsLinkApiDetail.as_view(), name="newslink-api-detail"),
    path("newslink/", NewsLinkApiList.as_view(), name="newslink_api_list"),
]
