from django.contrib import admin
from blog.models import Post, BlogComment

admin.site.register((BlogComment))

@admin.register(Post)
class EditorAdmin(admin.ModelAdmin):
    class Media:
        js = ('tinyadmin.js',)