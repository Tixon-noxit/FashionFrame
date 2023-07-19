from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User, Group


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title')
    prepopulated_fields = {"slug": ("title",)}


class GalleryInline(admin.TabularInline):
    fk_name = 'shooting'
    model = Gallery


class ShootingAdmin(admin.ModelAdmin):
    inlines = [GalleryInline, ]  #
    list_display = ('id', 'title', 'time_create', 'get_html_photo')  #
    list_display_links = ('id', 'title', 'get_html_photo')  #
    search_fields = ('id', 'title')  # Поиск по ...
    prepopulated_fields = {"slug": ("title",)}  #
    fields = ('category', 'title', 'slug', 'subtitle', 'miniature', 'description', 'get_html_photo')  #
    readonly_fields = ('time_create', 'time_update', 'get_html_photo')  #

    def get_html_photo(self, object):
        if object.miniature:
            return mark_safe(f'<img src="{object.miniature.url}" style="max-height: 100px;">')

    get_html_photo.short_description = "Миниатюра"


class BackgroungImagegAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title')


admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(BackgroungImage, BackgroungImagegAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Shooting, ShootingAdmin)
