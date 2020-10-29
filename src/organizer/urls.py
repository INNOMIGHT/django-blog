from django.urls import path
from .views import TagApiDetail, TagApiList, StartupApiList, StartupApiDetail


urlpatterns = [
    path("tag/<str:slug>/", TagApiDetail.as_view(), name="tag-api-detail"),
    path("tag/", TagApiList.as_view(), name="tag-api-list"),
    path("startup/", StartupApiList.as_view(), name="startup-api-list"),
    path("startup/<str:slug>/", StartupApiDetail.as_view(), name="startup-api-detail")
]
