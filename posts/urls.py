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
    path('post/<int:id>',views.post_detail),
    path('updatepost/<id>',views.post_update),
    path('createpost',views.post_create),
    path('delpost/<num>',views.post_delete),    	
    path('deletecomment/<int:id>/', views.commentDelete, name='commentDelete'),
    path('editcomment/<int:id>/', views.commentEdit, name='commentEdit'),
    path('detail/like_post/<id>',views.like_post ,name="like_post"),
    path('detail/dislike_post/<id>',views.dislike_post ,name="dislike_post"),
]    	


    
