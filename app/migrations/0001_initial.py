# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-26 14:37
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('bank', models.CharField(blank=True, max_length=50, null=True)),
                ('branch', models.CharField(blank=True, max_length=50, null=True)),
                ('acc_code', models.CharField(blank=True, max_length=50, null=True)),
                ('acc_name', models.CharField(blank=True, max_length=50, null=True)),
                ('acc_type', models.CharField(blank=True, max_length=50, null=True)),
                ('image', models.FileField(blank=True, null=True, upload_to=b'upload/bank')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'account',
                'verbose_name_plural': 'Account',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('type', models.CharField(choices=[(b'B', b'Blog'), (b'C', b'Course')], max_length=1)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'category',
                'verbose_name_plural': 'Category',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('fullname', models.CharField(blank=True, max_length=50, null=True)),
                ('position', models.CharField(blank=True, max_length=150, null=True)),
                ('profile', tinymce.models.HTMLField(blank=True, null=True)),
                ('image', models.FileField(blank=True, null=True, upload_to=b'upload/teacher')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'teacher',
                'verbose_name_plural': 'Teacher',
            },
        ),
    ]
