from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'rating', 'is_published', 'price', 'time_create', 'category']
    list_editable = ['price', 'rating']


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name']
    ordering = ['id']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_editable = ['name']
    ordering = ['id']
