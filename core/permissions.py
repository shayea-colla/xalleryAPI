from rest_framework.permissions import BasePermission, SAFE_METHODS

from .debug import debug


def debug(message):
    print()
    print("-" * 150)
    print()
    print(message)
    print()
    print("-" * 150)
    print()


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permissions(self, request, view, obj):
        return obj.owner == request.user


class IsAccountOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj == request.user
