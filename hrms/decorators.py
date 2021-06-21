
from django.core.exceptions import PermissionDenied
from employee.models import User

def user_is_superuser(function):
    def wrap(request, *args, **kwargs):
        user = User.objects.get(id=request.user.id)
        if user.is_superuser:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    return wrap


def user_is_staff(function):
    def wrap(request, *args, **kwargs):
        user = User.objects.get(id=request.user.id)
        if user.is_superuser==False and user.is_staff:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    return wrap

