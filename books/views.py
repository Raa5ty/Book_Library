from django.shortcuts import render
from django.db.models import Count, Avg, Q
from .models import Book, Publisher, Store, Review

def books_list(request):
    """Простой список всех книг с аннотацией среднего рейтинга"""
    books = Book.objects.select_related('author', 'publisher').prefetch_related('genre', 'stores', 'reviews').annotate(
        avg_rating=Avg('reviews__rating'),
        reviews_count=Count('reviews')
    )
    return render(request, 'books/books_list.html', {'books': books})

def search_queries(request):
    """Страница с выполнением всех сложных запросов из задания PRO"""
    
    # Запрос 1: Книги, опубликованные издательствами из России
    books_by_country = Book.objects.filter(
        publisher__country='Россия'
    ).select_related('author', 'publisher').prefetch_related('genre')
    
    # Запрос 2: Книги, продающиеся в магазинах Москвы
    books_in_moscow = Book.objects.filter(
        stores__city='Москва'
    ).select_related('author', 'publisher').prefetch_related('genre', 'stores').distinct()
    
    # Запрос 3: Книги со средней оценкой выше 4.5
    high_rated_books = Book.objects.annotate(
        avg_rating=Avg('reviews__rating')
    ).filter(
        avg_rating__gt=4.5
    ).select_related('author', 'publisher').prefetch_related('genre', 'reviews')
    
    # Запрос 4: Количество книг в каждом магазине
    stores_with_book_count = Store.objects.annotate(
        book_count=Count('books')
    ).order_by('-book_count')
    
    # Запрос 5: Магазины, где продаются книги, изданные после 2010 года
    stores_with_recent_books = Store.objects.filter(
        books__published_date__year__gt=2010
    ).annotate(
        book_count=Count('books')
    ).distinct().order_by('-book_count')
    
    # Дополнительно: статистика для информации
    stats = {
        'total_books': Book.objects.count(),
        'total_stores': Store.objects.count(),
        'total_publishers': Publisher.objects.count(),
        'total_reviews': Review.objects.count(),
    }
    
    context = {
        'books_by_country': books_by_country,
        'books_in_moscow': books_in_moscow,
        'high_rated_books': high_rated_books,
        'stores_with_book_count': stores_with_book_count,
        'stores_with_recent_books': stores_with_recent_books,
        'stats': stats,
    }
    
    return render(request, 'books/search_queries.html', context)