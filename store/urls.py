from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [
    path('',views.Home,name="home"),
    path('register/',views.RegistrationView,name="register"),
    path('login/',views.loginView,name="login"),
]
