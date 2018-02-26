# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-26 14:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app', '0001_initial'),
        ('taggit', '0002_auto_20150616_2121'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=80)),
                ('slug', models.SlugField(blank=True, max_length=150, null=True)),
                ('title', models.CharField(blank=True, max_length=150, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('lessons', models.IntegerField(default=0)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=15)),
                ('image', models.FileField(blank=True, null=True, upload_to=b'upload/video')),
                ('published', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Category')),
                ('tags', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
                ('teacher', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Teacher')),
            ],
            options={
                'db_table': 'video',
                'verbose_name_plural': 'Video',
            },
        ),
        migrations.CreateModel(
            name='VideoPlaylist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.IntegerField()),
                ('chapter', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('time', models.CharField(blank=True, max_length=20, null=True)),
                ('preview', models.BooleanField(default=False)),
                ('link', models.URLField(blank=True, null=True)),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='video.Video')),
            ],
            options={
                'db_table': 'video_playlist',
                'verbose_name_plural': 'VideoPlaylist',
            },
        ),
    ]