from posts.models import Post

def all_posts(**kwargs):
  """
  Get Post objects.

  :params: kwargs for filtering
  :return: list of Post (queryset)
  """
  return Post.objects.filter(**kwargs).all()

def get_post(id):
  try:
    return Post.objects.get(id=id)
  except Post.DoesNotExist:
    return None

def create_post(title, contents):
  post = Post(title=title, contents=contents)
  post.save()
  return post