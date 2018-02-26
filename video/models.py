from django.db import models
from taggit.managers import TaggableManager

from app.models import Category, Teacher


class Video(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=80)
    slug = models.SlugField(max_length=150, null=True, blank=True)
    title = models.CharField(max_length=150, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Category, null=True, blank=True)
    teacher = models.ForeignKey(Teacher, null=True, blank=True)
    lessons = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    image = models.FileField(upload_to='upload/video', null=True, blank=True)
    tags = TaggableManager(blank=True)
    published = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'video'
        verbose_name_plural = 'Video'

    def __unicode__(self):
        return self.name


class VideoPlaylist(models.Model):
    video = models.ForeignKey(Video)
    no = models.IntegerField()
    chapter = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    time = models.CharField(max_length=20, null=True, blank=True)
    preview = models.BooleanField(default=False)
    link = models.URLField(max_length=200, null=True, blank=True)

    class Meta:
        db_table = 'video_playlist'
        verbose_name_plural = 'VideoPlaylist'

    def __unicode__(self):
        return self.title
