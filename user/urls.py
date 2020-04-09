from django.urls import path

from user import views

urlpatterns = [
    path("get_all_user/", views.get_all_user, name="get_all_user"),
    path("add_user/", views.add_user, name="add_user"),
    path("edit_user/", views.edit_user, name="edit_user"),
    path("user_distribution/", views.user_distribution, name="user_distribution"),
    path("user_register_trend/", views.user_register_trend, name="user_register_trend"),
]
