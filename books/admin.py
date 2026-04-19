from django.contrib import admin
from .models import Author, Book, Genre

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date')
    filter_horizontal = ('genre',)  # Удобный виджет для ManyToMany

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
