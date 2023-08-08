from django.urls import path
from album.views import *
from django.contrib.auth import views as auth_views

urlpatterns = [

    # path('api/albums/list', albums_api_list, name='albums_api_list'),
    # path('api/album/detail/<int:pk>', album_api_detail, name='album_api_detail'),
    #
    # path('api/photos/list', photos_api_list, name='photos_api_list'),
    # path('api/photo/detail/<int:pk>', photo_api_detail, name='photo_api_detail'),

    # path('api/v1/albums/', AlbumAPIList.as_view()),
    # path('api/v1/album/<int:pk>/', AlbumAPIUpdate.as_view()),
    # path('api/v1/albumdelete/<int:pk>/', AlbumAPIDestroy.as_view()),
    #
    # path('api/v1/photos/', PhotoAPIList.as_view()),
    # path('api/v1/photo/<int:pk>/', PhotoAPIUpdate.as_view()),
    # path('api/v1/photodelete/<int:pk>/', PhotoAPIDestroy.as_view()),

    path('albums/', AlbumAPIList.as_view()),
    path('album/<int:pk>/', AlbumAPIUpdate.as_view()),
    path('albumdelete/<int:pk>/', AlbumAPIDestroy.as_view()),

    path('photos/', PhotoAPIList.as_view()),
    path('photo/<int:pk>/', PhotoAPIUpdate.as_view()),
    path('photodelete/<int:pk>/', PhotoAPIDestroy.as_view()),

    path('categories/', CategoryAPIList.as_view()),
    path('category/<int:pk>/', CategoryAPIUpdate.as_view()),
    path('categorydelete/<int:pk>/', CategoryAPIDestroy.as_view()),



]