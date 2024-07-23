from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow authors of a post to edit it.
    """
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the author of the post.
        return obj.author == request.user


class IsAdminOrSelf(permissions.BasePermission):
    """
    Custom permission to only allow admins to create or edit users,
    and allow users to edit their own information.
    """

    def has_permission(self, request, view):
        # Allow GET requests for all logged-in users
        if request.method in permissions.SAFE_METHODS:
            return request.user.is_authenticated

        # Disallow POST requests (user creation)
        if request.method == 'POST':
            return False

        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Allow GET requests for all logged-in users
        if request.method in permissions.SAFE_METHODS:
            return request.user.is_authenticated

        # Allow PATCH/PUT requests only for the user's own information
        if request.method in ['PUT', 'PATCH']:
            return obj == request.user

        # Disallow DELETE requests (user deletion)
        if request.method == 'DELETE':
            return False

        return False
