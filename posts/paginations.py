from rest_framework.pagination import PageNumberPagination
from posts.models import Post

class PostPagination(PageNumberPagination):
    page_size = 2
