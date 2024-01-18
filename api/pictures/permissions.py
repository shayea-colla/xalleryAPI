from rest_framework.permissions import BasePermission, SAFE_METHODS
from django.contrib.auth.models import Group

from gallery.utils import debug


class PicturePermissions(BasePermission):
    """
    All the permission logic of Picture model and picture viewset should live here.

    __Picture permissions specifications:
        - Read for All users ( authenticated and Non authenticated )
        - Write for Desingers
    """

    def has_permission(self, request, view):
        # Read for All users
        if request.method in SAFE_METHODS:
            return True

        return request.user.is_designer()

    def has_object_permission(self, request, view, obj):
        return request.user.is_owner(obj)
