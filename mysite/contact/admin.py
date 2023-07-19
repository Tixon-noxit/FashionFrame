from django.contrib import admin
from .models import *


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'phone', 'time_create', )
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title')


class AlertContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title')


admin.site.register(AlertContact, AlertContactAdmin)
admin.site.register(Contact, ContactAdmin)