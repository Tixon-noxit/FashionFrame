from django.db import models
from django.urls import reverse


class CategoryBlog(models.Model):
    title = models.CharField(max_length=100, verbose_name='Категория')  # Название Категории
    description = models.TextField(max_length=500, blank=True, verbose_name='Описание')  # Описание Категории
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')  # Слаг для отображения
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания категории')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения категории')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('main:blog:blog', kwargs={'blog_slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['time_create', 'title']


class Article(models.Model):  # Класс Статья
    category = models.ForeignKey(CategoryBlog, on_delete=models.CASCADE, verbose_name='Категория')  # Категория статьи
    miniature = models.ImageField(upload_to="miniature_blog/%Y/%m/%d", verbose_name='Миниатюра', blank=True)  # Миниатюра Статьи
    title = models.CharField(max_length=100, verbose_name='Название статьи')  # Название Статьи
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')  # Слаг для отображения
    short_description = models.TextField(max_length=1000, verbose_name='Краткое описание', blank=True)  # Краткое описание
    description = models.TextField(max_length=10000, blank=True, verbose_name='Текст статьи')  # Текст статьи
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания съемки')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения съемки')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('main:blog:article', kwargs={'article_slug': self.slug})

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['time_create', 'title']


class Hashtag(models.Model):
    text = models.CharField(max_length=250, blank=True, verbose_name='Хештег статьи')  # Абзац статьи
    hashtag = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='hashtag')

    class Meta:
        verbose_name = 'Хештег'
        verbose_name_plural = 'Хештеги'


class Paragraph(models.Model):
    text = models.TextField(max_length=500, blank=True, verbose_name='Aбзац статьи')  # Абзац статьи
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='paragraph')

    class Meta:
        verbose_name = 'Абзац'
        verbose_name_plural = 'Абзацы'

