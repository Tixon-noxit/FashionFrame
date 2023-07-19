from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import CategoryPrice, AlertPrice


class CategoryPriceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title')


class AlertPriceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title')


admin.site.register(CategoryPrice, CategoryPriceAdmin)
admin.site.register(AlertPrice, AlertPriceAdmin)

