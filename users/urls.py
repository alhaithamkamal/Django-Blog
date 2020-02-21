from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/',views.register , name='register'),
    path('login/',views.login_view , name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name="users/logout.html"),name='logout'),
    path("profile/",views.profile , name="profile"),
    path('blocked/',views.blocked,name="blocked"),
    path("profile/edit/",views.edit_profile , name="edit_profile"),
    path("password/change/",views.change_password , name="change_password")
    ]
