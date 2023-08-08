import django_filters
from .models import Album, Photo, Category
from django_filters import CharFilter, NumberFilter, DateTimeFilter


class AlbumFilter(django_filters.FilterSet):
    # album_title = CharFilter(field_name='album_title', lookup_expr='icontains', label='Поиск по названию альбома')

    album_pub_date = DateTimeFilter(field_name='album_pub_date', lookup_expr='exact')
    album_pub_date_gte = DateTimeFilter(field_name='album_pub_date', lookup_expr='gte')
    album_pub_date_lte = DateTimeFilter(field_name='album_pub_date', lookup_expr='lte')
    album_pub_date_gt = DateTimeFilter(field_name='album_pub_date', lookup_expr='gt')
    album_pub_date_lt = DateTimeFilter(field_name='album_pub_date', lookup_expr='lt')

    photos_quantity = NumberFilter(field_name='photos_quantity', lookup_expr='exact')
    photos_quantity_gte = NumberFilter(field_name='photos_quantity', lookup_expr='gte')
    photos_quantity_lte = NumberFilter(field_name='photos_quantity', lookup_expr='lte')
    photos_quantity_gt = NumberFilter(field_name='photos_quantity', lookup_expr='gt')
    photos_quantity_lt = NumberFilter(field_name='photos_quantity', lookup_expr='lt')

    class Meta:
        model = Album
        fields = ['album_pub_date', 'photos_quantity']


class PhotoFilter(django_filters.FilterSet):
    # album_title = CharFilter(field_name='album__title', lookup_expr='icontains', label='Поиск по названию альбома')

    category = CharFilter(field_name='category', lookup_expr='icontains', label='Поиск по категории')

    photo_pub_date = DateTimeFilter(field_name='photo_pub_date', lookup_expr='exact')
    photo_pub_date_gte = DateTimeFilter(field_name='photo_pub_date', lookup_expr='gte')
    photo_pub_date_lte = DateTimeFilter(field_name='photo_pub_date', lookup_expr='lte')
    photo_pub_date_gt = DateTimeFilter(field_name='photo_pub_date', lookup_expr='gt')
    photo_pub_date_lt = DateTimeFilter(field_name='photo_pub_date', lookup_expr='lt')

    class Meta:
        model = Photo
        fields = ['category', 'photo_pub_date']

        # exclude = ('album', 'tag')