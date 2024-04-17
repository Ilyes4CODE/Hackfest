from functools import wraps
from rest_framework.response import Response
from rest_framework import status
import random

def check_ban_status(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        # Assuming the request.user is authenticated
        if request.user.is_authenticated:
            profile = request.user.profile
            if profile.is_banned:
                return Response({"error": "You are banned from accessing this resource."}, status=status.HTTP_403_FORBIDDEN)
        return view_func(request, *args, **kwargs)
    return _wrapped_view

def generate_verification_code():
    return ''.join(random.choices('0123456789', k=6))

def group_required(group_name):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            if request.user.is_authenticated and request.user.groups.filter(name=group_name).exists():
                return view_func(request, *args, **kwargs)
            else:
                return Response({"Error": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)
        return wrapper
    return decorator