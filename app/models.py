from django.db import models
from tinymce.models import HTMLField


CATEGORY_CHOICE = (
    ('B', 'Blog'),
    ('C', 'Course'),
)


class Account(models.Model):
    name = models.CharField(max_length=50)
    bank = models.CharField(max_length=50, null=True, blank=True)
    branch = models.CharField(max_length=50, null=True, blank=True)
    acc_code = models.CharField(max_length=50, null=True, blank=True)
    acc_name = models.CharField(max_length=50, null=True, blank=True)
    acc_type = models.CharField(max_length=50, null=True, blank=True)
    image = models.FileField(upload_to='upload/bank', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'account'
        verbose_name_plural = 'Account'

    def __unicode__(self):
        return self.name


class Category(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=50, null=True, blank=True)
    type = models.CharField(max_length=1, choices=CATEGORY_CHOICE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'category'
        verbose_name_plural = 'Category'

    def __unicode__(self):
        return self.name


class Teacher(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=50, null=True, blank=True)
    fullname = models.CharField(max_length=50, null=True, blank=True)
    position = models.CharField(max_length=150, null=True, blank=True)
    profile = HTMLField(null=True, blank=True)
    image = models.FileField(upload_to='upload/teacher', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'teacher'
        verbose_name_plural = 'Teacher'

    def __unicode__(self):
        return self.name
