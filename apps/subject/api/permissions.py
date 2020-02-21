from rest_framework import permissions


class ReworkPermission(permissions.IsAuthenticated):
    # TODO fill permissions
    def has_permission(self, request, view):
        return super(ReworkPermission, self).has_permission(request, view)

    def has_object_permission(self, request, view, obj):
        return super(ReworkPermission, self).has_object_permission(request, view, obj)
