# from django.shortcuts import render, get_object_or_404, redirect
# from django.http import HttpResponse, HttpResponseRedirect
#
# from django.http import JsonResponse

#
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
#
#
# @api_view(['GET', 'POST'])
# def albums_api_list(request):
#     if request.method == 'GET':
#         albums_list = Album.objects.all()
#         serializer = AlbumSerializer(albums_list, many=True)
#         # return JsonResponse({'albums_list': serializer.data})
#         return Response({'albums_list': serializer.data})
#     elif request.method == 'POST':
#         serializer = AlbumSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def album_api_detail(request, pk, format=None):
#     album_obj = get_object_or_404(Album, pk=pk)
#     if album_obj.exist:
#         if request.method == 'GET':
#             serializer = AlbumSerializer(album_obj)
#             return Response(serializer.data)
#         elif request.method == 'PUT':
#             serializer = AlbumSerializer(album_obj, data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response({'message': "Данные успешно изменены", 'album': serializer.data})
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         elif request.method == 'DELETE':
#             album_obj.delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)
#     else:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#
# @api_view(['GET', 'POST'])
# def photos_api_list(request):
#     if request.method == 'GET':
#         photos_list = Photo.objects.all()
#         serializer = PhotoSerializer(photos_list, many=True)
#         # return JsonResponse({'albums_list': serializer.data})
#         return Response({'photos_list': serializer.data})
#     elif request.method == 'POST':
#         serializer = PhotoSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def photo_api_detail(request, pk, format=None):
#     photo_obj = get_object_or_404(Photo, pk=pk)
#     if photo_obj.exist:
#         if request.method == 'GET':
#             serializer = PhotoSerializer(photo_obj)
#             return Response(serializer.data)
#         elif request.method == 'PUT':
#             serializer = PhotoSerializer(photo_obj, data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response({'message': "Данные успешно изменены", 'album': serializer.data})
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         elif request.method == 'DELETE':
#             photo_obj.delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)
#     else:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#
#
#
# @api_view(['GET', 'POST'])
# def album_users_api_list(request):
#     if request.method == 'GET':
#         users_list = User.objects.all()
#         serializer = UserSerializer(users_list, many=True)
#         # return JsonResponse({'albums_list': serializer.data})
#         return Response({'users_list': serializer.data})
#     elif request.method == 'POST':
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['GET', 'POST'])
# def album_category_api_list(request):
#     if request.method == 'GET':
#         categories_list = Category.objects.all()
#         serializer = CategorySerializer(categories_list, many=True)
#         # return JsonResponse({'albums_list': serializer.data})
#         return Response({'categories_list': serializer.data})
#     elif request.method == 'POST':
#         serializer = CategorySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# from django.forms import model_to_dict
from rest_framework import generics, viewsets, mixins
# from django.shortcuts import render
# from rest_framework.decorators import action
# from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
# from rest_framework.response import Response
# from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
#
#
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter, SearchFilter

# from .filters import CustomAlbumFilter, CustomPhotoFilter

from .models import Album, Photo, User, Category
from .serializer import AlbumSerializer, PhotoSerializer, CategorySerializer
from django.shortcuts import render
from .filters import AlbumFilter, PhotoFilter

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.filters import OrderingFilter, SearchFilter




class AlbumAPIList(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    # permission_classes = (IsOwnerOrReadOnly, )

    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)

    # filterset_class = AlbumFilter
    filterset_fields = ['album_pub_date', 'photos_quantity']
    # search_fields = ('album_title',)
    # ordering_fields = ('album_title', 'album_pub_date', 'photos_quantity')

    def get_queryset(self):
        """Показать альбомы пользователя"""
        return Album.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """При создании альбома владельцем становится тот, кто его создал."""
        if self.request.user.is_authenticated:
            instance = serializer.save(user=self.request.user)



class AlbumAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    # permission_classes = (IsOwnerOrReadOnly, )


class AlbumAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    # permission_classes = (IsOwnerOrReadOnly, )



class PhotoAPIList(generics.ListCreateAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    # permission_classes = (IsOwnerOrReadOnly, )

    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterset_fields = ['category', 'photo_pub_date']
    # class_filter = PhotoFilter
    # search_fields = ('album_title', 'category', 'photo_pub_date',)
    # ordering_fields = ('album_title', 'category', 'photo_pub_date')

    # def get_queryset(self):
    #     return Photo.objects.filter(album=self.request.user)

class PhotoAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    # permission_classes = (IsOwnerOrReadOnly, )


class PhotoAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    # permission_classes = (IsOwnerOrReadOnly, )


class CategoryAPIList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # permission_classes = (IsOwnerOrReadOnly, )


class CategoryAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # permission_classes = (IsOwnerOrReadOnly, )


class CategoryAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # permission_classes = (IsOwnerOrReadOnly, )


