from django.urls import path, include 

urlpatterns = [
    path(r"", include("api.rooms.urls")),
    path(r"", include("api.pictures.urls")),
    path(r"", include("api.order.urls")),
    path(r"accounts/", include("accounts.api.urls")),
    path(r"tags/", include("api.tags.urls")),
    path(r"auth/", include("api.knox_auth.urls")),

]
