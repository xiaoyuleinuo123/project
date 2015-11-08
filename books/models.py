from django.db import models

# Create your models here.

class Author(models.Model):
    AuthorID = models.IntegerField(max_length=10)
    Name = models.CharField(max_length=40)
    Age = models.IntegerField(max_length=3)
    Country = models.CharField(max_length=40)

class Book(models.Model):
    ISBN = models.CharField(max_length=20)
    Title = models.CharField(max_length=100)
    #AuthorID = models.ForeignKey(Author)
    AuthorID = models.IntegerField(max_length=10)
    #authors = models.ManyToManyField(Author)
    Publisher = models.CharField(max_length=20)
    PublishDate = models.DateField()
    Price = models.IntegerField(max_length=10)
