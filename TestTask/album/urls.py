from django.urls import path
from album.views import *

urlpatterns = [
    path('albums/', AlbumAPIList.as_view()),
    path('album/<int:pk>/', AlbumAPIUpdate.as_view()),
    path('delete_album/<int:pk>/', AlbumAPIDestroy.as_view()),

    path('photos/', PhotoAPIList.as_view()),
    path('photo/<int:pk>/', PhotoAPIUpdate.as_view()),
    path('delete_photo/<int:pk>/', PhotoAPIDestroy.as_view()),

    path('categories/', CategoryAPIList.as_view()),
    path('category/<int:pk>/', CategoryAPIUpdate.as_view()),
    path('delete_category/<int:pk>/', CategoryAPIDestroy.as_view()),
]
