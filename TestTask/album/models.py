from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFit

from album.validators import image_validator


class Album(models.Model):
    album_title = models.CharField(max_length=120, default='Альбом', unique=True, verbose_name='Наименование альбома')
    description = models.TextField(blank=True, null=True, verbose_name='Описание альбома')
    album_pub_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания альбома')
    photos_quantity = models.PositiveIntegerField(default=0, verbose_name='Количество фотографий в альбоме')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name='Автор альбома')

    def __str__(self):
        return 'Альбом: ' + self.album_title

    def get_absolute_url(self):
        return reverse('the_album', kwargs={'album_id': self.pk})

    class Meta:
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'
        ordering = ['album_title']

    def get_fields(self):
        return [(field.verbose_name, field.value_from_object(self)) for field in self.__class__._meta.fields]


class Photo(models.Model):
    image_file = models.FileField(null=True, blank=True, upload_to='image/%Y/%m/%d', validators=[image_validator], verbose_name='Фотография')
    photo_pub_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    category = models.ManyToManyField('Category', verbose_name='Категория фотографии', related_name='photo_category')
    album = models.ForeignKey('Album', on_delete=models.CASCADE, verbose_name='Альбом фотографии', related_name='album_photos')
    thumbnail = ImageSpecField(source='image_file', processors=[ResizeToFit(width=150, height=150, upscale=None, mat_color=None, anchor='c')], format="PNG", options={'quality': 60})

    def __str__(self):
        return 'Фотография: ' + str(self.pk)

    def get_absolute_url(self):
        return reverse('the_photo', kwargs={'photo_id': self.pk})

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'
        ordering = ['photo_pub_date']


class Category(models.Model):
    cat_title = models.CharField(max_length=30, default='Категория', verbose_name='Категория фотографии')

    def __str__(self):
        return 'Категория: ' + self.cat_title

    def get_absolute_url(self):
        return reverse('the_category', kwargs={'category_id': self.pk})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категория'
        ordering = ['cat_title']

    def get_fields(self):
        return [(field.verbose_name, field.value_from_object(self)) for field in self.__class__._meta.fields]
