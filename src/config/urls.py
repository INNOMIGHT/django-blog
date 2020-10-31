from django.contrib import admin
from django.urls import path, include

from organizer.routers import urlpatterns as organizer_api_urls
from blog.routers import url_patterns as blog_api_urls

api_urls = blog_api_urls + organizer_api_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(api_urls))
]
