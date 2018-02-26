from django.db import models
from taggit.managers import TaggableManager

from app.models import Category, Teacher


def get_book_sample(instance, filename):
    return 'upload/book/%s/sample/%s' % (instance.code, filename)


def get_book_image(instance, filename):
    return 'upload/book/%s/images/%s' % (instance.code, filename)


class Book(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=150, null=True, blank=True)
    slug = models.SlugField(max_length=150, null=True, blank=True)
    option = models.CharField(max_length=150, null=True, blank=True)
    preview = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Category, null=True, blank=True)
    teacher = models.ForeignKey(Teacher, null=True, blank=True)
    pages = models.IntegerField(default=0)
    year = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    price_ebook = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    sample = models.FileField(upload_to=get_book_sample, null=True, blank=True)
    image = models.FileField(upload_to=get_book_image, null=True, blank=True)
    published = models.BooleanField(default=True)
    tags = TaggableManager(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'book'
        verbose_name_plural = 'Book'

    def __unicode__(self):
        return self.title
