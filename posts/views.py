from django.shortcuts import render
from django.http.response import JsonResponse

from posts.services import get_posts, create_post

def index(request):
  posts = get_posts()

  data = [{
    "id": post.id,
    "title": post.title,
    "contents": post.contents
  } for post in posts]

  return JsonResponse(data, safe=False)

def detail(request, pk=None):
  post = get_posts(id=pk)
  if (len(post) == 0): return JsonResponse({}, status=404)
  if (len(post) != 1): return JsonResponse({}, status=400)
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
    
