from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsSuperUserOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True

        return bool(
            request.user.is_superuser and request.user.is_authenticated
        )


class IsSuperUserOrAuthor(BasePermission):

    def has_permission(self, request, view):
        return bool(
            (request.user.is_superuser and request.user.is_authenticated) or
            (request.user.is_authenticated and request.user.author)
        )


class IsSuperUserOrAuthorOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        return bool(
            request.user.is_authenticated and request.user.is_superuser or
            request.user.is_authenticated and obj.author == request.user
        )