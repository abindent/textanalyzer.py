from django.contrib import admin

from .models import Blog, Comment

# Register your models here.
admin.site.register((Comment))

@admin.register(Blog)
class EditorAdmin(admin.ModelAdmin):
    class Media:
        js = ['utils/tinyadmin.js',]

