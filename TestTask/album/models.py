import os
import sys

from django.db import models
from django.db.models import F, ExpressionWrapper, DecimalField
from django.urls import reverse
from django.forms.utils import ErrorList
from imagekit.models import ImageSpecField, ProcessedImageField
from pilkit.processors import ResizeToFill, ResizeToFit

from album.validators import image_validator

from django.conf import settings
from django.contrib.auth.models import User

from django.db.models import Count



class Album(models.Model):
    album_title = models.CharField(max_length=120, default='Альбом', unique=True, null=False, verbose_name='Наименование альбома')
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

    @property
    def quantity(self):
        return Photo.objects.filter(photos_quantity=self.photos_quantity).count()






    # @property
    # def quantity(self):
    #     # def quantity(self):
    #     #     return Album.objects.filter(author=self).aggregate(
    #     #         photos_quantity=Count('photos_quantity')
    #     #     )['count']
    #     photos_quantity = Photo.objects.filter().count()
    #     return photos_quantity


    # exist = models.BooleanField(default=True, null=True)
    # class Poll(models.Model):
    #     choices_count = models.IntegerField()  # To store num of choices.

    # def update_choices_count(self):
    #     self.photos_quantity = self.photo_set.count()
    #     self.save()

    # class Poll(models.Model):
    #     ...
    #


    # @property
    # def quantity(self):
    #     return self.photos_quantity.count()

    # @property
    # def quantity(self):
    #     return Photo.objects.filter().count()
    # @property
    # def quantity(self):
    #     return album_object.photos.count()

    # return Element.objects.filter(name=self.name).count()



class Photo(models.Model):
    image_file = models.FileField(null=True, blank=True, upload_to='image/%Y/%m/%d', validators=[image_validator], verbose_name='Фотография')

    photo_pub_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    category = models.ManyToManyField('Category', verbose_name='Категория фотографии', related_name='photo_category')
    album = models.ForeignKey('Album', on_delete=models.CASCADE, verbose_name='Альбом фотографии', related_name='album_photos')

    # thumbnail = models.ImageField(upload_to='images/thumbnails', blank=True, verbose_name='Миниатюра')
    thumbnail = ImageSpecField(source='image_file', processors=[ResizeToFit(width=150, height=150, upscale=None, mat_color=None, anchor='c')], format="PNG", options={'quality': 60})

    def __str__(self):
        return 'Фотография: ' + str(self.pk)

    def get_absolute_url(self):
        return reverse('the_photo', kwargs={'photo_id': self.pk})

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'
        ordering = ['album']











    # class Choice(models.Model):
    #     poll = models.ForeignKey(Poll, related_name="choices")
    # album_object.photos.count()



    # def get_fields(self):
    #     return [(field.verbose_name, field.value_from_object(self)) for field in self.__class__._meta.fields]


# picture = Photo.objects.all()[0]
# print(picture.avatar_thumbnail.url)  # > /media/CACHE/images/982d5af84cddddfd0fbf70892b4431e4.jpg
# print(picture.avatar_thumbnail.width)
#     @staticmethod
#     def save(self):
#         if not self.pk:
#             Album.objects.filter(pk=self.album_id).update(photos_quantity=F('photos_quantity') + 1)
#         super(Photo, self).save()
#
#     @staticmethod
#     def delete(self):
#         if self.album_id and self.album.photos_quantity > 0:
#             Album.objects.filter(pk=self.album_id).update(photos_quantity=F('photos_quantity') - 1)
#         super(Photo, self).delete()


# class User(models.Model):
#     pass
#     name = models.CharField(max_length=30, default='Фамилия пользователя', null=False, verbose_name='Фамилия пользователя')
#     surname = models.CharField(max_length=30, default='Имя пользователя', null=False, verbose_name='Имя пользователя')
#
#     def __str__(self):
#         return ': ' + self.name
#
#     def get_absolute_url(self):
#         return reverse('the_user', kwargs={'author_id': self.pk})
#
#     class Meta:
#         verbose_name = 'Пользователь'
#         verbose_name_plural = 'Пользователи'
#         ordering = ['name']

#     def get_fields(self):
#         return [(field.verbose_name, field.value_from_object(self)) for field in self.__class__._meta.fields]


class Category(models.Model):
    _meta = None
    cat_title = models.CharField(max_length=30, default='Категория', null=False, verbose_name='Категория фотографии')

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