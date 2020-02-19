from django.contrib import admin
from .models import Profile

class UserProfileAdmin(admin.ModelAdmin):
    list_display =['user','is_locked','undesired_words_count']
admin.site.register(Profile,UserProfileAdmin)
