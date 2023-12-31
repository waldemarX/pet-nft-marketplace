from django.contrib import admin
from .models import Post, Categories


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'author',
        'pub_date',
        'category',
        'is_published'
    )
    search_fields = ['title']
    list_editable = (
        'category',
        'is_published'
    )
    list_filter = ('pub_date',)


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = (
        'category_name',
        'slug'
    )
    search_fields = ['category_name']
    prepopulated_fields = {'slug': ('category_name',)}
