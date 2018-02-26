from django.db import models
from tinymce.models import HTMLField
from taggit.managers import TaggableManager

from app.models import Category, Teacher


COURSE_STATUS_CHOICE = (
    ('P', 'Publish'),
    ('A', 'Almost'),
    ('F', 'Full'),
    ('C', 'Complete'),
)


def get_course_outline(instance, filename):
    return 'upload/course/%s/outline/%s' % (instance.code, filename)


def get_course_image(instance, filename):
    return 'upload/course/%s/images/%s' % (instance.code, filename)


class Course(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, null=True, blank=True)
    preview = models.TextField(null=True, blank=True)
    description = HTMLField(null=True, blank=True)
    category = models.ForeignKey(Category, null=True, blank=True)
    teacher = models.ForeignKey(Teacher, null=True, blank=True)
    hours = models.IntegerField(default=0)
    days = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    outline = models.FileField(upload_to=get_course_outline, null=True, blank=True)
    image = models.FileField(upload_to=get_course_image, null=True, blank=True)
    tags = TaggableManager(blank=True)
    published = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'course'
        verbose_name_plural = 'Course'

    def __unicode__(self):
        return self.name


class CourseOpen(models.Model):
    course = models.ForeignKey(Course)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=150, null=True, blank=True)
    schedule = models.CharField(max_length=50, null=True, blank=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    promotion = models.CharField(max_length=50, null=True, blank=True)
    status = models.CharField(max_length=1, choices=COURSE_STATUS_CHOICE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'course_open'
        verbose_name_plural = 'CourseOpen'

    def __unicode__(self):
        return self.name
