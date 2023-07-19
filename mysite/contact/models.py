from django.db import models


class Contact(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')  # Название Категории
    description = models.TextField(max_length=500, blank=True, verbose_name='Подзаголовок')  # Описание Категории
    brief_information = models.TextField(max_length=500, blank=True, verbose_name='Краткая информация')
    email = models.EmailField(verbose_name='Email')
    phone = models.CharField(max_length=15, verbose_name='Телефон для связи')
    adress = models.CharField(max_length=255, verbose_name='Адрес', blank=True)
    instagramm_link = models.CharField(max_length=255, verbose_name='Ссылка на Инстаграмм', blank=True)
    facebook_link = models.CharField(max_length=255, verbose_name='Ссылка на FaceBook', blank=True)
    twitter_link = models.CharField(max_length=255, verbose_name='Ссылка на Twitter', blank=True)
    Vk_link = models.CharField(max_length=255, verbose_name='Ссылка на VK', blank=True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания контактных данных')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения контактных данных')

    def __str__(self):
        return self.brief_information

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'
        ordering = ['time_create', 'title']


class AlertContact(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(max_length=1500, blank=True, verbose_name='Содержание')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания alert')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения alert')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Оповещение'
        verbose_name_plural = 'Оповещения'
        ordering = ['time_create', 'title']


class ContactMessage(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    telephone = models.CharField(max_length=15)
    message = models.TextField(max_length=1000)

    def __str__(self):
        # Будет отображаться следующее поле в панели администрирования
        return self.email

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
