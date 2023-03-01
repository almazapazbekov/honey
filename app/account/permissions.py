from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAuthorPermission(BasePermission):
    def has_permission(self, request, view):
        if bool(request.user and request.user.is_authenticated):
            return True

    def has_object_permission(self, request, view, obj):
        if bool(
                request.user and request.user.is_authenticated and obj == request.user):
            return True


class NoRegisterPermission(BasePermission):
    def has_permission(self, request, view):
        if bool(request.user and request.user.is_authenticated):
            return False
        else:
            return True

    def has_object_permission(self, request, view, obj):
        if bool(
                request.user and request.user.is_authenticated and obj == request.user):
            return False
        else:
            return True