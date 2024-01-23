from rest_framework.routers import SimpleRouter
from .viewsets import PictureViewSet


router = SimpleRouter()
router.register(r"pictures", PictureViewSet, basename="picture")
urlpatterns = router.urls
