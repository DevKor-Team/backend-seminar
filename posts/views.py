from rest_framework import decorators, status, mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from django.http import Http404

from posts.serializer import PostSerializer
from posts.services import all_posts, get_post, create_post, update_post, delete_post

class PostViewSet(GenericViewSet):
    authentication_classes = []
    permission_classes = []

    serializer_class = PostSerializer

    queryset = all_posts()

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        title = request.data.get("title")
        contents = request.data.get("contents")
        if not title:
            return Response(status=400)
        create_post(title, contents)
        return Response({"success": True})

    def retrieve(self, request, pk=None, *args, **kwargs):
        post = self.get_object()
        serializer = self.get_serializer(post)
        return Response(serializer.data)

    def update(self, request, pk=None, *args, **kwargs):
        post = self.get_object()
        serializer = self.get_serializer(post, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None, *args, **kwargs):
        post = self.get_object()
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @decorators.action(methods=["GET", "POST"], detail=True)
    def like(self, request, pk=None, *args, **kwargs):
        post = self.get_object()
        if request.method == "GET":
            return Response({"like": post.likes})
        elif request.method == "POST":
            post.likes += 1
            post.save()
        return Response({"like": post.likes})
