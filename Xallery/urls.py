"""
URL configuration for Xallery project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView
from api.order.views import HomePageOrder

from rest_framework.authtoken import views

urlpatterns = [
    path("", RedirectView.as_view(url="/gallery/")),
    path("admin/", admin.site.urls),
    path("gallery/", include("gallery.urls")),
    path("accounts/", include("accounts.urls")),
    path("order/", HomePageOrder.as_view(), name="order-home"),
    # API urls
    path("api/", include("api.rooms.urls")),
    path("api/", include("api.pictures.urls")),
    path("api/", include("api.order.urls")),
    path("api/designers/", include("api.designers.urls")),
    # rest_framework Token auth endpoint
    path("api/authtoken/", views.obtain_auth_token),
    # Experment Application for testing purposes
    path("exper/", include("exper.urls")),
]

# Serving images during development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
