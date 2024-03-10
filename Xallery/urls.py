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
    path(r"", RedirectView.as_view(url="/api/")),
    path(r"api/", include("api.urls")),
    path('api-auth/', include('rest_framework.urls')),
]


#    path(r"order/", HomePageOrder.as_view(), name="order-home"),
#    path(r"gallery/", include("gallery.urls")),
#    path(r"accounts/", include("accounts.urls")),
#    path(r"admin/", admin.site.urls),

# Serving images during development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
