from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    rating = models.FloatField()
    author = models.ForeignKey('Author', on_delete=models.PROTECT, null=True)
    description = models.TextField(blank=False)
    price = models.FloatField()
    time_create = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='category')

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=255, verbose_name='name')
    last_name = models.CharField(max_length=255, verbose_name='surname')
    bio = models.TextField(blank=True)
    birth_day = models.DateField()

    def __str__(self):
        return self.first_name


