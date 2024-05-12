from rest_framework import permissions

from .permissions import IsDrinkEditorPermission

class DrinkEditorPermissionMixin():
    permission_classes = [
        permissions.IsAuthenticated,
        IsDrinkEditorPermission
    ]


class DrinkQuerySetMixin():
    public_field = "public"
    allow_staff_view = False

    def get_queryset(self, *args, **kwargs):
        user = self.request.user
        qs = super().get_queryset(*args, **kwargs)
        if self.allow_staff_view and user.is_staff:
            return qs
        return qs.filter(public=True)


class UserQuerySetMixin():
    user_field = 'debtor'
    allow_staff_view = False

    def get_queryset(self, *args, **kwargs):
        user = self.request.user
        lookup_data = {}
        lookup_data[self.user_field] = user
        qs = super().get_queryset(*args, **kwargs)
        if self.allow_staff_view and user.is_staff:
            return qs
        return qs.filter(**lookup_data)