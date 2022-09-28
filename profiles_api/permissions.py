from rest_framework import permissions
 

class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profile"""


    def has_object_permission(self, request, view, obj):
        """check user if trying to edit their own prfile"""
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.id == request.user.id


class UpdateOwnStatus(permissions.BasePermission):
    """Allow users to updated own status"""


    def has_object_permisssion(self, request, view, obj):
        """Check the user is trying to update own status"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id