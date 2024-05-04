from rest_framework import permissions

from .permissions import IsDrinkEditorPermission

class DrinkEditorPermissionMixin():
    permission_classes = [
        permissions.IsAdminUser,
        IsDrinkEditorPermission
    ]