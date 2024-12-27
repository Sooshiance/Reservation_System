from django.urls import path

from club import views


app_name = "club"

urlpatterns = [
    path("faq/", views.seeQuestion, name="faq"),
    path("trains/", views.allTrain, name="trains"),
    path("rating/<str:pk>/", views.sendComment, name="rating"),
]
