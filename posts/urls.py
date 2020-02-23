from django.contrib import admin
from django.urls import path
from posts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.posts),
    path('detail',views.post_detail),
    path('list',views.post_list),
]    	

