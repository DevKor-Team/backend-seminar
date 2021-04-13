from django.shortcuts import render
from django.http.response import JsonResponse
from django.http import QueryDict

from posts.services import all_posts, get_post, create_post, update_post, delete_post

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

def update(request, pk=None):
    post = update_post(
      id=pk,
      title=QueryDict(request.body).get("title"),
      contents=QueryDict(request.body).get("contents")
    )
    if post is None: return JsonResponse({}, status=404)
    return JsonResponse({"success": True})

def delete(request, pk=None):
    success = delete_post(pk)
    return JsonResponse({"success": success})

def post(request, pk=None):
  if request.method == "GET":
    return detail(request, pk)
  if request.method == "PATCH":
    return update(request, pk)
  if request.method == "DELETE":
    return delete(request, pk)