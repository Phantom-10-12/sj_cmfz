from django.urls import path

from main import views

urlpatterns = [
    path("index/", views.index, name="index"),
    path("login/", views.login, name="login"),
    path("login_logic/", views.login_logic, name="login_logic"),
    path("get_captcha/", views.get_captcha, name="get_captcha"),
]
