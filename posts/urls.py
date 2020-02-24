from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.posts),
    path('list/',views.post_list, name= 'post_list'),
    path('detail/<int:id>/',views.post_detail, name='post_detail'),
    path('create/', views.post_create, name='post_create'),
    path('edit/<int:id>/', views.post_edit, name= 'post_edit'),
    path('like/',views.like_post, name="like_post"),

    ]


    