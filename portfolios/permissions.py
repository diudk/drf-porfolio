from rest_framework import permissions

from portfolios.models import Portfolio


class BasePermissionOwnerOrReadOnly(permissions.BasePermission):

    def new_rule(self, request, view, obj):
        return True

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return self.new_rule(request, view, obj)


class IsPortfolioOwnerOrReadOnly(BasePermissionOwnerOrReadOnly):
    def new_rule(self, request, view, obj):
        if hasattr(obj, 'user_created'):
            return obj.user_created == request.user
        return False


class IsPhotoOwnerOrReadOnly(BasePermissionOwnerOrReadOnly):
    def new_rule(self, request, view, obj):
        if hasattr(obj, 'portfolio'):
            return obj.portfolio in Portfolio.objects.filter(user_created=request.user).all()
        return False


