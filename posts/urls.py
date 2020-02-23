from django.contrib import admin
from django.urls import path
from posts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.posts),
    path('detail/<num>',views.post_detail),
    path('list',views.post_list),
    path('update/<id>',views.post_update),
    path('create',views.post_create),
    path('del/<id>',views.post_delete),
]    	

