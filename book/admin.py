from django.contrib import admin
from .models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'option', 'category', 'teacher', 'pages', 'year', 'published']
    search_fields = ['code', 'name']
    prepopulated_fields = {'slug': ['name']}

admin.site.register(Book, BookAdmin)
