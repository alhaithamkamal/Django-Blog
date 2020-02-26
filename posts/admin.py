from django.contrib import admin
from posts.models import Post
# # Register your models here.
class CustomPost(admin.ModelAdmin):
	fieldsets = (['write post', {'fields': ['title', 'body','image','user','status']}],
		['like or dislike',{'fields':['likes','dislikes']}],)
	list_display = ['title','image','date_published','slug_url','status','id']
	list_filter =['date_published','title']
	

admin.site.register(Post,CustomPost)
# Register your models here.
