from django.db import models


class About(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')  # Название Категории
    description = models.TextField(max_length=500, blank=True, verbose_name='Подзаголовок')  # Описание Категории
    left_column = models.TextField(verbose_name='Левая колонка текста')
    right_column = models.TextField(verbose_name='Правая колонка текста')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания контактных данных')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения контактных данных')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Обо мне'
        verbose_name_plural = 'Обо мне'
        ordering = ['time_create', 'title']
