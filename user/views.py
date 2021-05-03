from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

from user.services import authenticate, login, logout, create_user
from user.decorators import require_username_password

class SignUpView(APIView):
    authentication_classes = []
    permission_classes = []

    @require_username_password
    def post(self, request, username, password):
        user = create_user(username, password)

        if user is None:
            return Response({"success": False}, status=status.HTTP_400_BAD_REQUEST)

        login(request, user)
    
        return Response({"success": True})


class LoginView(APIView):
    authentication_classes = []
    permission_classes = []

    @require_username_password
    def post(self, request, username, password):
        user = authenticate(username=username, password=password)
        if user is None:
            return Response({"success": False, "error": "match user not found."}, status=status.HTTP_404_NOT_FOUND)
        else:
            login(request, user)

        return Response({"success": True})

class LogoutView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        logout(request)
        return Response({"success": True})

