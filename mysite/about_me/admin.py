from django.contrib import admin
from .models import *


class AboutMeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title')


admin.site.register(About, AboutMeAdmin)
