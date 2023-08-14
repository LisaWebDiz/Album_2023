from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets
from rest_framework.filters import OrderingFilter, SearchFilter


from .filters import AlbumFilter, PhotoFilter
from .models import Album, Photo, Category
from .serializer import AlbumSerializer, PhotoSerializer, CategorySerializer


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterset_fields = ['album_pub_date']
    filterset_class = AlbumFilter

    def get_queryset(self):
        return Album.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            instance = serializer.save(user=self.request.user)


class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterset_fields = ['category', 'photo_pub_date']
    filterset_class = PhotoFilter

    def get_queryset(self):
        return Photo.objects.filter(album__user=self.request.user)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


