from django.urls import path

from main import views

urlpatterns = [
    path("main/", views.main, name="main"),
]