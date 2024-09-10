from django.urls import path

from user import views


app_name = "user"

urlpatterns = [
    path("", views.loginUser, name='login'),
    path("profile/", views.userProfile, name='profile'),
    path("logout/", views.logoutUser, name='logout'),
    path("register/", views.registerUser, name='register'),
]
