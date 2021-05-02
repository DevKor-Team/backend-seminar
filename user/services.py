from django.contrib.auth import authenticate, login, logout
from user.models import User

def create_user(username, password):
  try:
    return User.objects.create_user(username=username, password=password)
  except:
    return None
