from django.urls import path

from posts import views

urlpatterns = [
    path('', views.index),
    path('create/', views.create),
    path('<int:pk>/', views.post),
]
