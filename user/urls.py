from django.urls import path

from user import views

urlpatterns = [
    path('signup', views.SignUpView.as_view()),
    path('login', views.LoginView.as_view()),
    path('logout', views.LogoutView.as_view()),
]
