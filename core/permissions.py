from rest_framework.permissions import BasePermission, SAFE_METHODS


from core.debug import debug
from core.utils import is_designer


class IsObjectOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        return obj.owner == request.user


class IsAccountOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj == request.user


class IsDesignerOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        debug("is Designer or Read Only")
        if request.method in SAFE_METHODS:
            return True

        debug("is Designer or Read Only")
        return is_designer(request.user)


class IsDesigner(BasePermission):
    def has_permission(self, request, view):
        return is_designer(request.user)
