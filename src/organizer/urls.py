from django.urls import path
from .views import TagApiDetail, TagApiList


urlpatterns = [
    path("<str:slug>/", TagApiDetail.as_view(), name="tag-api-detail"),
    path("", TagApiList.as_view(), name="tag-api-list"),
]
