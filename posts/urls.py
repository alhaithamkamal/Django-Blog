from django.urls import path
from posts import views

urlpatterns = [
    path('', views.posts),
    path('detail/<num>',views.post_detail),
    path('list',views.post_list),
    path('update/<id>',views.post_update),
    path('create',views.post_create),
    path('del/<num>',views.post_delete),
]    	

