from django.contrib import admin

from .models import Course, CourseOpen


class CourseAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'category', 'hours', 'days', 'price', 'published']
    search_fields = ['code', 'name']
    prepopulated_fields = {'slug': ['name']}


class CourseOpenAdmin(admin.ModelAdmin):
    list_display = ['name', 'schedule', 'location', 'price', 'status']
    search_fields = ['name']


admin.site.register(Course, CourseAdmin)
admin.site.register(CourseOpen, CourseOpenAdmin)
