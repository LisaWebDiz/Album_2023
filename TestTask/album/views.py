from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import generics
from rest_framework.filters import OrderingFilter, SearchFilter

from .models import Album, Photo, Category
from .serializer import AlbumSerializer, PhotoSerializer, CategorySerializer


class AlbumAPIList(generics.ListCreateAPIView):
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


class AlbumAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class AlbumAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class PhotoAPIList(generics.ListCreateAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterset_fields = ['category', 'photo_pub_date']
    filterset_class = PhotoFilter
    
    def get_queryset(self):
        return Photo.objects.filter(user=self.request.user)


class PhotoAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer


class PhotoAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer


class CategoryAPIList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
