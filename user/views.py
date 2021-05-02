from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

from user.services import authenticate, login, create_user
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

