from rest_framework.permissions import BasePermission



class IsAdminRole(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == "ADMIN"
    


class IsCandidateRole(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == "CANDIDATE"
    


class IsViewerRole(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role in ["VIEWER", "ADMIN", "CANDIDATE"]
    