from rest_framework import permissions
from core.debug import debug


class IsOwner(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an 'orderer' and 'receiver' attribute
    """

    def has_object_permission(self, request, view, obj):
        return obj.orderer == request.user


class IsOwnerOrReceiver(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an 'orderer' and 'receiver' attribute
    """

    def has_object_permission(self, request, view, obj):
        return obj.orderer == request.user or obj.receiver == request.user


class CanDeleteOrder(permissions.BasePermission):
    """
    Object-level permission to only allow receiver of an object to edit it.
    Assumes the model instance has an 'orderer' and 'receiver' attribute
    """

    def has_object_permission(self, request, view, obj):
        return obj.orderer == request.user
