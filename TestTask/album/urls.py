from django.urls import path
from album.views import *

urlpatterns = [
    path('albums/', AlbumAPI.as_view(), name='albums_api_list'),
    path('album/<int:pk>/', AlbumAPI.as_view()),
    path('delete_album/<int:pk>/', AlbumAPI.as_view()),

    path('photos/', PhotoAPI.as_view(), name='photos_api_list'),
    path('photo/<int:pk>/', PhotoAPI.as_view()),
    path('delete_photo/<int:pk>/', PhotoAPI.as_view()),

    path('categories/', CategoryAPI.as_view()),
    path('category/<int:pk>/', CategoryAPI.as_view()),
    path('delete_category/<int:pk>/', CategoryAPI.as_view()),
]
