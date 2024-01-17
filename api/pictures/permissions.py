from rest_framework.permissions import BasePermission, SAFE_METHODS



class IsRoomOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, object):
        if request.method in SAFE_METHODS:
            return True
        else:
            return request.user == object.room.owner


class IsObjectOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, object):
        if request.method in SAFE_METHODS:
            return True
        else:
            return request.user == object.owner

