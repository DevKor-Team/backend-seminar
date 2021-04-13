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

def update_post(id, title=None, contents=None):
  post = get_post(id)
  if post is None: return None
  post.title = title if title is not None else post.title
  post.contents = contents if contents is not None else post.contents
  post.save()
  return post
