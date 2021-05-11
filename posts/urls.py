from django.urls import path, include
from rest_framework import routers

from posts import views

router = routers.DefaultRouter()
router.register("", views.PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

# urlpatterns = router.urls
