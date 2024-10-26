from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100, verbose_name="Cтроковое поле для имени автора")
    birthdate = models.DateField(verbose_name="Поле даты для дня рождения автора")

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Genre(models.Model):
    name = models.CharField(max_length=100, verbose_name="На")
    books = models.ManyToManyField(Book, related_name='genres')

    def __str__(self):
        return self.name
