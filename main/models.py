from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Book(models.Model):
    """Model class

    Fields:
      name - Book title
      description - Short description
      author - Author of the book
      year - Year published
      pages - Number of pages
      rating - Book rating
      slug - Field for url
    """
    name = models.CharField(max_length=30, default='name')
    author = models.CharField(max_length=30, default='autor')
    year = models.IntegerField(default=2015)
    pages = models.IntegerField(default=320)
    rating = models.IntegerField(default=7)
    description = models.CharField(max_length=400, default='description')
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        """Save model and convert name field to slug field"""
        if not self.id:
            self.slug = slugify(self.name)
        super(Book, self).save(*args, **kwargs)

    def __str__(self):
        """Return name"""
        return self.name

    def get_absolute_url(self):
        """Reverse kwargs={'pk': self.pk}"""
        return reverse('book_edit', kwargs={'pk': self.pk})