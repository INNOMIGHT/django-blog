from django.urls import path
from rest_framework.routers import SimpleRouter
from .viewsets import TagViewSet, StartupViewSet, NewslinkViewset


class NewsLinkRouter(SimpleRouter):
    """Override the SimpleRouter for articles
    DRF's routers expect there to only be a single variable
    for finding objects. However, our NewsLinks needs
    two! We therefore override the Router's behavior to
    make it do what we want.
    The big question: was it worth switching to a ViewSet
    and Router over our previous config for this?
    """

    def get_lookup_regex(self, *args, **kwargs):
        """Return regular expression pattern for URL path
        This is the (rough) equivalent of the simple path:
            <str:startup_slug>/<str:newslink_slug>
        """
        return (
            r"(?P<startup_slug>[^/.]+)/"
            r"(?P<newslink_slug>[^/.]+)"
        )


api_router = SimpleRouter()
api_router.register("tag", TagViewSet, base_name="tag-api")
api_router.register("startup", StartupViewSet, base_name="startup-api")
nl_router = NewsLinkRouter()
nl_router.register("newslink", NewslinkViewset, base_name="newslink-api")

api_routes = api_router.urls + nl_router.urls

urlpatterns = api_routes
