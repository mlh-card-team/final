from django.contrib import admin
from .models import Post,Image

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','author','publish','status')
    list_filter = ('status', 'publish','author')
    search_fields = ('title', 'body')
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status','publish')

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
	ordering = ('title','image')


