from rest_framework.viewsets import ViewSet
from rest_framework import decorators
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

from posts.serializer import PostSerializer
from posts.services import all_posts, get_post, create_post, update_post, delete_post

class PostViewSet(ViewSet):
  authentication_classes = []
  permission_classes = []

  queryset = all_posts()

  def get_object(self, pk):
    post = get_post(pk)
    if post is None:
      raise Http404
    return post

  def list(self, request, *args, **kwargs):
    serializer = PostSerializer(self.queryset.all(), many=True)
    return Response(serializer.data)

  def create(self, request, *args, **kwargs):
    title = request.data.get("title")
    contents = request.data.get("contents")
    if not title: return Response(status=400)
    create_post(title, contents)
    return Response({"success": True})

  def retrieve(self, request, pk=None, *args, **kwargs):
    post = self.get_object(pk)
    serializer = PostSerializer(post)
    return Response(serializer.data)

  def update(self, request, pk=None, *args, **kwargs):
    post = self.get_object(pk)
    serializer = PostSerializer(post, data=request.data, partial=True)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def destroy(self, request, pk=None, *args, **kwargs):
    post = self.get_object(pk)
    post.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
