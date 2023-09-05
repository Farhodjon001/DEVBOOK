from rest_framework.permissions import BasePermission

class BookCreateUpdatePermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.roles in (1,2)
class AuthorCreateUpdatePermissions(BasePermission):
    def has_permission(self, request, view):
        return request.user.roles==1

class AuthorUpdatePermissions(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user==request.user

