from django.db import models
from django.urls import reverse


class CategoryPrice(models.Model):
    miniature = models.ImageField(upload_to="miniature_price/%Y/%m/%d", verbose_name='Миниатюра',
                                  blank=True)  # Миниатюра Ценника
    title = models.CharField(max_length=100, verbose_name='Название услуги')  # Название Категории
    description = models.TextField(max_length=1500, blank=True, verbose_name='Содержание')
    # slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')  # Слаг для отображения
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания услуги')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения услуги')

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('main:blog:blog', kwargs={'blog_slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['time_create', 'title']


class AlertPrice(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(max_length=1500, blank=True, verbose_name='Содержание')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания alert')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения alert')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Подвал Жанны'
        verbose_name_plural = 'Подвалы Жанны'
        ordering = ['time_create', 'title']

