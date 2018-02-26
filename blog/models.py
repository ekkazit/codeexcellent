from django.db import models
from tinymce.models import HTMLField
from taggit.managers import TaggableManager

from app.models import Category, Teacher


class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=150, null=True, blank=True)
    content = HTMLField(null=True, blank=True)
    category = models.ForeignKey(Category, null=True, blank=True)
    teacher = models.ForeignKey(Teacher, null=True, blank=True)
    image = models.FileField(upload_to='upload/post', null=True, blank=True)
    published = models.BooleanField(default=True)
    tags = TaggableManager(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'post'
        verbose_name_plural = 'Post'

    def __unicode__(self):
        return self.title
