from rest_framework.permissions import BasePermission, SAFE_METHODS
from gallery.utils import debug


class IsRoomOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, object):
        # Allow Read Only for users other than the owner

        if request.method in SAFE_METHODS:
            return True

        return request.user == object.owner
