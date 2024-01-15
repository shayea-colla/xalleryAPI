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

urlpatterns = [
    path("", RedirectView.as_view(url="/gallery/")),
    path("gallery/", include("gallery.urls")),
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("order/", HomePageOrder.as_view(), name="order-home"),
    # API urls
    path("api/", include("api.rooms.urls")),
    path("api/order/", include("api.order.urls")),
    path("api/designers/", include("api.designers.urls")),
    # Experment Application for testing and learning new things
    path("exper/", include("exper.urls")),
]

# Serving images during development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
