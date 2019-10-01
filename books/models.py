from django.db import models
from django.urls import reverse

class Book(models.Model):
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    date_published = models.DateField()
    number_of_pages = models.IntegerField()

    type_of_book = (
        ('Nov', 'Novel'),
        ('Doc', 'Documentation'),
        ('Mag', 'Magazine'),
    )
##    name = models.CharField(max_length=60)
    type_of_book = models.CharField(max_length=10, choices=type_of_book)
    

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book_edit', kwargs={'pk': self.pk})
