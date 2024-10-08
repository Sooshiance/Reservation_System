from django.urls import path

from booking import views


app_name = "booking"

urlpatterns = [
    path("", views.home, name="home"),

    path("reserve/", views.userReserveTicketView, name='reserve'),

    path('delete/<int:pk>/', views.userDeleteTicketView, name='delete'),
]
