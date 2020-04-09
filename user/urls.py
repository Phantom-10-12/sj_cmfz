from django.urls import path

from user import views

urlpatterns = [
    path("get_all_user/", views.get_all_user, name="get_all_user"),
    path("add_user/", views.add_user, name="add_user"),
    path("edit_user/", views.edit_user, name="edit_user"),
]
