from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

from posts.serializer import PostSerializer
from posts.services import all_posts, get_post, create_post, update_post, delete_post

class PostListCreateView(APIView):
  authentication_classes = []
  permission_classes = []

  queryset = all_posts()

  def get(self, request):
    serializer = PostSerializer(self.queryset.all(), many=True)
    return Response(serializer.data)

  def post(self, request):
    title = request.data.get("title")
    contents = request.data.get("contents")
    if not title: return Response(status=400)
    create_post(title, contents)
    return Response({"success": True})

class PostDetailView(APIView):
  authentication_classes = []
  permission_classes = []

  def get_object(self, pk):
    post = get_post(pk)
    if post is None:
      raise Http404
    return post

  def get(self, request, pk, format=None):
      post = self.get_object(pk)
      serializer = PostSerializer(post)
      return Response(serializer.data)

  def put(self, request, pk, format=None):
      post = self.get_object(pk)
      serializer = PostSerializer(post, data=request.data)
      if serializer.is_valid():
          serializer.save()
          return Response(serializer.data)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk, format=None):
      post = self.get_object(pk)
      post.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)