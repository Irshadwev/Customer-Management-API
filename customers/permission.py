from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsStaffOrReadOnly(BasePermission):

    def has_permission(self, request, view):

        # User must be authenticated
        if not request.user or not request.user.is_authenticated:
            return False

        # Staff/admin can do everything
        if request.user.is_staff:
            return True

        # Normal authenticated users can only read
        return request.method in SAFE_METHODS