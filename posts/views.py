from rest_framework.views import APIView
from rest_framework.response import Response

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
