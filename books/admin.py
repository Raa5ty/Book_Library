from django.contrib import admin
from .models import Author, Genre, Book, Publisher, Store, Review

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')
    list_filter = ('country',)
    search_fields = ('name',)

@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'city')
    list_filter = ('city',)
    search_fields = ('name',)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('book', 'rating', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('book__title',)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publisher', 'published_date')
    list_filter = ('published_date', 'publisher', 'genre')
    search_fields = ('title', 'author__name')
    filter_horizontal = ('genre', 'stores')  # Удобные виджеты для ManyToMany
    raw_id_fields = ('author', 'publisher')  # Для оптимизации при большом количестве записей