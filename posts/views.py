from django.shortcuts import render
from django.http.response import JsonResponse

from posts.services import all_posts, get_post, create_post

def index(request):
  posts = all_posts()

  data = [{
    "id": post.id,
    "title": post.title,
    "contents": post.contents
  } for post in posts]

  return JsonResponse(data, safe=False)

def detail(request, pk=None):
  post = get_post(id=pk)
  if post is None: return JsonResponse({}, status=404)

  return JsonResponse({
    "title": post.title,
    "contents": post.contents,
  })

def create(request):
  if request.method == "POST":
    title = request.POST.get("title")
    contents = request.POST.get("contents")
    if not title: return JsonResponse({}, status=400)
    create_post(title, contents)
    return JsonResponse({"success": True})
