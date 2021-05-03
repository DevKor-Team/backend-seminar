from django.db.models import Q
from django_filters import rest_framework as filters
from posts.models import Post

class PostFilter(filters.FilterSet):
    title = filters.CharFilter(
        field_name='title',
        label='제목',
    )
    contents = filters.CharFilter(
        field_name='contents',
        label='제목+내용',
        method='get_contents'
    )

    @staticmethod
    def get_contents(queryset, name, value):
        return queryset.filter(
            Q(contents__contains=value) |
            Q(title__contains=value)
        )

    class Meta:
        model = Post
        fields = {
            'title': [
                'contains'
            ],
        }

