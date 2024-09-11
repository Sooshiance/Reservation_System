from django.urls import path

from club import views


urlpatterns = [
    path("faq/", views.seeQuestion, name='faq'),
    path("trains/", views.allTrain, name='tains'),
    path("raing/<int:pk>/", views.sendComment, name='rating'),
]