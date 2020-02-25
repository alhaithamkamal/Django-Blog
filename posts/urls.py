from django.urls import path
from posts import views

urlpatterns = [
    path('', views.posts),
    path('subscribe/<cat_id>', views.subscribe),
    path('unsubscribe/<cat_id>', views.unsubscribe),
    path('category/<cat_id>', views.categoryPosts),
    path('tag/<tag_id>', views.tagPosts),
    path('search', views.search),
    path('about', views.about),
    path('post/<post_id>',views.post_detail),
    path('updatepost/<id>',views.post_update),
    path('createpost',views.post_create),
    path('delpost/<num>',views.post_delete),
]    	


