from django.db import models
from django.urls import reverse


class BackgroungImage(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(max_length=500, blank=True, verbose_name='Описание')
    miniature = models.ImageField(upload_to="background/%Y/%m/%d", verbose_name='Фото')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания категории')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения категории')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Фоновое фото'
        verbose_name_plural = 'Фоновые фото'
        ordering = ['time_create', 'title']


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='Категория')  # Название Категории
    description = models.TextField(max_length=500, blank=True, verbose_name='Описание')  # Описание Категории
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')  # Слаг для отображения
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания категории')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения категории')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('main:category', kwargs={'category_slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['time_create', 'title']


class Shooting(models.Model):  # Класс съемки
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')  # Указать категорию
    title = models.CharField(max_length=100, verbose_name='Съемка')  # Название съемки
    model = models.CharField(max_length=255, blank=True)  # Имя модели
    subtitle = models.CharField(max_length=100, verbose_name='Краткое описание', blank=True)  # Краткое описание съемки
    miniature = models.ImageField(upload_to="miniature/%Y/%m/%d", verbose_name='Миниатюра')  # Миниатюра съемки
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')  # Слаг для отображения
    description = models.TextField(max_length=500, blank=True, verbose_name='Описание')  # Описание съемки
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания съемки')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения съемки')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('main:shooting', kwargs={'shooting_slug': self.slug})

    class Meta:
        verbose_name = 'Съемка'
        verbose_name_plural = 'Съемки'
        ordering = ['time_create', 'title']


class Gallery(models.Model):
    image = models.ImageField(upload_to='photo_gallery')
    shooting = models.ForeignKey(Shooting, on_delete=models.CASCADE, related_name='photos')

    class Meta:
        verbose_name = 'Фото'


