from django.contrib import admin
from django.urls import path, include

from organizer.routers import urlpatterns as organizer_api_urls
from blog.routers import url_patterns as blog_api_urls
from organizer.urls import urlpatterns as organizer_urls
from blog.urls import urlpatterns as blog_urls

api_urls = blog_api_urls + organizer_api_urls
view_urls = organizer_urls + blog_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(api_urls)),
    path("", include(view_urls))
]
