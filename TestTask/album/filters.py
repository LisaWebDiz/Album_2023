import django_filters
from django_filters import CharFilter, NumberFilter, DateTimeFilter

from .models import Album, Photo

class AlbumFilter(django_filters.FilterSet):
    album_title = CharFilter(field_name='album_title', lookup_expr='icontains', label='Поиск в названии альбома')

    album_pub_date_gte = DateTimeFilter(field_name='album_pub_date', lookup_expr='gte', label='Дата создания: точная или позже')
    album_pub_date_lte = DateTimeFilter(field_name='album_pub_date', lookup_expr='lte', label='Дата создания: точная или раньше')

    class Meta:
        model = Album
        fields = ['album_title', 'album_pub_date']


class PhotoFilter(django_filters.FilterSet):
    photo_pub_date_gte = DateTimeFilter(field_name='photo_pub_date', lookup_expr='gte', label='Дата создания: точная или позже')
    photo_pub_date_lte = DateTimeFilter(field_name='photo_pub_date', lookup_expr='lte', label='Дата создания: точная или раньше')

    class Meta:
        model = Photo
        fields = ['photo_pub_date']
