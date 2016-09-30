from django.db import models


class Article(models.Model):
    class Meta:
        db_table = 'Article'

    header = models.TextField(max_length=150)
    text = models.TextField()
    picture = models.ImageField()
    date = models.DateField(auto_now=True)


class Person(models.Model):
    class Meta:
        db_table = 'Person'

    name = models.TextField(max_length=30)
    surname = models.TextField(max_length=30)
    years = models.TextField()
    picture = models.ImageField()
    text = models.TextField()

    def __str__(self):
        return self.name


class Place(models.Model):
    class Meta:
        db_table = 'Place'

    name = models.TextField()
    text = models.TextField()
    picture = models.ImageField()

    def __str__(self):
        return self.name
