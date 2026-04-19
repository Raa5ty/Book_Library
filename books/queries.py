import os
import django

# Настройка Django окружения для запуска скрипта
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'book_library.settings')
django.setup()

from .models import Author, Book, Genre
from django.db.models import Count

def run_queries():
    print("=" * 50)
    print("ЗАДАНИЕ: Выполнение запросов")
    print("=" * 50)
    
    # 1. Найдите все книги, которые принадлежат жанру "Фантастика"
    print("\n1. Книги жанра 'Фантастика':")
    print("-" * 30)
    try:
        fantasy_books = Book.objects.filter(genre__name='Фантастика')
        if fantasy_books.exists():
            for book in fantasy_books:
                print(f"  - {book.title} (Автор: {book.author.name})")
        else:
            print("  Книги жанра 'Фантастика' не найдены")
    except Exception as e:
        print(f"  Ошибка: {e}")
    
    # 2. Найдите все книги, которые принадлежат одновременно жанрам "Фантастика" и "Роман"
    print("\n2. Книги жанров 'Фантастика' и 'Роман' одновременно:")
    print("-" * 30)
    try:
        fantasy_novel_books = Book.objects.filter(
            genre__name='Фантастика'
        ).filter(
            genre__name='Роман'
        )
        if fantasy_novel_books.exists():
            for book in fantasy_novel_books:
                print(f"  - {book.title} (Автор: {book.author.name})")
                genres = ", ".join([g.name for g in book.genre.all()])
                print(f"    Жанры: {genres}")
        else:
            print("  Книги, принадлежащие одновременно обоим жанрам, не найдены")
    except Exception as e:
        print(f"  Ошибка: {e}")
    
    # 3. Подсчитайте количество книг в каждом жанре
    print("\n3. Количество книг в каждом жанре:")
    print("-" * 30)
    try:
        genres_with_count = Genre.objects.annotate(book_count=Count('books'))
        for genre in genres_with_count:
            print(f"  {genre.name}: {genre.book_count} книг(а/и)")
    except Exception as e:
        print(f"  Ошибка: {e}")
    
    # Дополнительно: показать все книги с их жанрами для наглядности
    print("\n" + "=" * 50)
    print("ДОПОЛНИТЕЛЬНО: Все книги с жанрами")
    print("=" * 50)
    try:
        all_books = Book.objects.all().prefetch_related('genre', 'author')
        if all_books.exists():
            for book in all_books:
                genres = ", ".join([g.name for g in book.genre.all()]) if book.genre.exists() else "Жанры не указаны"
                print(f"\n  📚 {book.title}")
                print(f"     Автор: {book.author.name}")
                print(f"     Жанры: {genres}")
        else:
            print("  В базе данных нет книг")
    except Exception as e:
        print(f"  Ошибка: {e}")

if __name__ == "__main__":
    run_queries()
    
'''
# Для запроса в терминале:

python manage.py shell

# Импортируем модели
from books.models import Author, Book, Genre
from django.db.models import Count

# 1. Книги жанра "Фантастика"
fantasy_books = Book.objects.filter(genre__name='Фантастика')
for book in fantasy_books:
    print(book.title, book.author.name)

# 2. Книги жанров "Фантастика" И "Детектив" одновременно
fantasy_detective = Book.objects.filter(genre__name='Фантастика').filter(genre__name='Детектив')
for book in fantasy_detective:
    print(book.title, [g.name for g in book.genre.all()])

# 3. Количество книг в каждом жанре
genres = Genre.objects.annotate(book_count=Count('books'))
for genre in genres:
    print(f"{genre.name}: {genre.book_count}")

'''