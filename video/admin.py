from django.contrib import admin

from .models import Video, VideoPlaylist


class VideoPlaylistInline(admin.TabularInline):
    model = VideoPlaylist
    extra = 0


class VideoAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'category', 'lessons', 'price', 'published']
    search_fields = ['code', 'name']
    inlines = [VideoPlaylistInline]


admin.site.register(Video, VideoAdmin)
