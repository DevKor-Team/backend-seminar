from rest_framework import decorators
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from posts.filters import PostFilter
from posts.paginations import PostPagination
from posts.serializer import PostSerializer
from posts.services import all_posts

class PostViewSet(ModelViewSet):
    filterset_class = PostFilter
    pagination_class = PostPagination
    permission_classes = []

    serializer_class = PostSerializer

    queryset = all_posts()

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
