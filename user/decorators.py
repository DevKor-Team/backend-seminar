from rest_framework.response import Response
from rest_framework import status

def require_username_password(func):
    # for CBV methods
    def wrapper(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")
        if (username is None) or (password is None):
            return Response({"success": False, "error": "key error."}, status=status.HTTP_400_BAD_REQUEST)
        return func(self, request, username, password, *args, **kwargs)
    return wrapper
