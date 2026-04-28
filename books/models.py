from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название издательства")
    country = models.CharField(max_length=100, verbose_name="Страна")

    class Meta:
        verbose_name = "Издательство"
        verbose_name_plural = "Издательства"

    def __str__(self):
        return f"{self.name} ({self.country})"

class Store(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название магазина")
    city = models.CharField(max_length=100, verbose_name="Город")

    class Meta:
        verbose_name = "Магазин"
        verbose_name_plural = "Магазины"

    def __str__(self):
        return f"{self.name} ({self.city})"

class Review(models.Model):
    book = models.ForeignKey('Book', on_delete=models.CASCADE, related_name='reviews', verbose_name="Книга")
    rating = models.PositiveSmallIntegerField(verbose_name="Оценка", help_text="Оценка от 1 до 5")
    comment = models.TextField(blank=True, verbose_name="Комментарий")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

    def __str__(self):
        return f"Отзыв на {self.book.title}: {self.rating}/5"

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    published_date = models.DateField()
    description = models.TextField(blank=True)
    genre = models.ManyToManyField(Genre, related_name='books', blank=True)
    
    publisher = models.ForeignKey(
        Publisher, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name='books',
        verbose_name="Издательство"
    )
    stores = models.ManyToManyField(
        Store, 
        related_name='books',
        blank=True,
        verbose_name="Магазины"
    )

    def __str__(self):
        return self.title