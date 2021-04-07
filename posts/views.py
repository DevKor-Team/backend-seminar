from django.shortcuts import render

from django.http.response import JsonResponse

def index(request):
  if request.method in ["GET", "POST"]:
    return JsonResponse({"req_method": request.method})
  else:
    return JsonResponse({"error": "method not allowed"})
