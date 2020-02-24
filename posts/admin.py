from django.contrib import admin
from .models import Post , Comment


# Register your models here.



class PostAdmin(admin.ModelAdmin):
	list_display = ('title','slug', 'user','published', 'status',)
	list_filter =  ('status','created','updated',)
	search_fildes = ('user__username','title',)
	prepopulated_fields = {'slug':('title',)}
	list_editable = ('status',)
	date_hierarchy =('created')


admin.site.register(Post,PostAdmin)
admin.site.register(Comment)


