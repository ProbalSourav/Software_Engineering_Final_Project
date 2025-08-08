from django.core.exceptions import PermissionDenied
from functools import wraps

def role_required(role_name):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped(request, *args, **kwargs):
            user = request.user
            if not user.is_authenticated:
                from django.contrib.auth.views import redirect_to_login
                return redirect_to_login(next=request.get_full_path())
            profile = getattr(user, 'profile', None)
            if not profile or profile.role != role_name:
                raise PermissionDenied
            if role_name in ('Patient', 'Doctor') and not profile.approved:
                raise PermissionDenied
            return view_func(request, *args, **kwargs)
        return _wrapped
    return decorator
