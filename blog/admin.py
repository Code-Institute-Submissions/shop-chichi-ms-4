from django.contrib import admin
from .models import Category, Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'intro',
        'article',
        'image',
        'data_added',
    )


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'title',
    )


class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'article',
        'data_added',
    )


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
