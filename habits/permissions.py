from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user == obj.owner:
            return True
        return False


class ReadOnly(BasePermission):
    """Разрешает только операции чтения."""

    def has_permission(self, request, view):
        return request.method in SAFE_METHODS
