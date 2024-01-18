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
        """
        The main reason for implementing this method is for the 'POST' request,
        since POST request doesn't call has_object_permission, I have to make
        that only designers is allowed to add new pictures
        """
        # Read for All users
        if request.method in SAFE_METHODS:
            return True

        return is_designer(request.user)

    def has_object_permission(self, request, view, obj):
        """
        Allow Non authenticated users and Normal users to "GET"
        the Picture Details, but restrict Dangerous action to only
        the Onwer of the Picture
        """
        if request.method in SAFE_METHODS:
            return True

        return is_owner(request.user, obj)


def is_designer(user: any) -> bool:
    designer_group = Group.objects.get(name="designers")
    return designer_group in user.groups.all()


def is_owner(user: any, obj: any) -> bool:
    return obj.owner == user
