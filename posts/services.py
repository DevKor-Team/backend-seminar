from posts.models import Post

def get_posts(**kwargs):
  """
  Get Post objects.

  :params: kwargs for filtering
  :return: list of Post (queryset)
  """
  return Post.objects.filter(**kwargs).all()