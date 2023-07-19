from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import CategoryBlog, Article, Paragraph, Hashtag


class CategoryBlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title')
    prepopulated_fields = {"slug": ("title",)}


class ParagraphInline(admin.TabularInline):
    fk_name = 'article'
    model = Paragraph


class HashtaghInline(admin.TabularInline):
    fk_name = 'hashtag'
    model = Hashtag


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'short_description', 'time_create', 'miniature')
    list_display_links = ('id', 'title', 'miniature')
    search_fields = ('id', 'title')
    prepopulated_fields = {"slug": ("title",)}  #
    fields = ('category', 'title', 'slug', 'short_description', 'miniature', 'description')  #
    readonly_fields = ('time_create', 'time_update', 'get_html_miniature')  #

    def get_html_miniature(self, object):
        if object.miniature:
            return mark_safe(f'<img src="{object.miniature_blog.url}" style="max-height: 100px;">')

    get_html_miniature.short_description = "Миниатюра"


admin.site.register(CategoryBlog, CategoryBlogAdmin)
admin.site.register(Article, ArticleAdmin)
