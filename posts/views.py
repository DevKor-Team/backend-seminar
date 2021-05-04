from rest_framework import decorators, status, mixins
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.response import Response
from django.http import Http404

from posts.filters import PostFilter
from posts.paginations import PostPagination
from posts.serializer import PostSerializer
from posts.services import all_posts, get_post, create_post, update_post, delete_post

class PostViewSet(GenericViewSet):
    filterset_class = PostFilter
    pagination_class = PostPagination
    permission_classes = []

    serializer_class = PostSerializer

    queryset = all_posts()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)

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

    @decorators.action(methods=["GET"], detail=True)
    def like(self, request, pk=None, *args, **kwargs):
        post = self.get_object()
        return Response({"like": post.likes})

    @like.mapping.post
    def post_like(self, request, pk=None):
        post = self.get_object()
        post.likes += 1
        post.save()
        return Response({"like": post.likes})
