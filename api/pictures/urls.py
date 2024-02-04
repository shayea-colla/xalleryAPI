from django.urls import include, path
from rest_framework.routers import SimpleRouter
from .viewsets import PictureViewSet
from .views import like_picture_view, unlike_picture_view


router = SimpleRouter()
router.register(r"pictures", PictureViewSet, basename="picture")
urlpatterns = [
        path("", include(router.urls)),
        path("pictures/<uuid:pk>/like/", like_picture_view, name='picture-like'),
        path("pictures/<uuid:pk>/unlike/", unlike_picture_view, name='picture-unlike'),
]
