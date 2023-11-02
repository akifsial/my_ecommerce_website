from django.contrib import admin
from django.urls import path
from store import views


urlpatterns = [
    path("", views.home, name = "home"),
    path("home/", views.home, name = "home"),
    path("store/", views.home, name = "home"),
    path("cart/", views.cart, name = "cart"),
    path("check-out/", views.checkOut, name = "check-out"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.login, name="login"),
    path("logout/", views.signout, name="signout"),
]