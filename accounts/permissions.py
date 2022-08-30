from accounts.models import User
from portfolios.permissions import BasePermissionOwnerOrReadOnly


class IsProfileOwnerOrReadOnly(BasePermissionOwnerOrReadOnly):
    def new_rule(self, request, view, obj):
        if isinstance(obj, User):
            return obj == request.user
        return False
