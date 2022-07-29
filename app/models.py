from django.db import models

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Book(models.Model):
    title =  models.CharField(max_length=100, blank=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"

class Edition(models.Model):
    year = models.PositiveSmallIntegerField(blank=False)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.book} Edition: {self.year}"