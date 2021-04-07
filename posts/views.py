from django.shortcuts import render
from django.http.response import JsonResponse

from posts.services import get_posts

def index(request):
  posts = get_posts()

  data = [{
    "id": post.id,
    "title": post.title,
    "contents": post.contents
  } for post in posts]

  return JsonResponse(data, safe=False)