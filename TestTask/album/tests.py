from os import walk

from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.db import transaction
from django.test import TestCase
from mixer.backend.django import mixer
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate

from album.models import Album
from .models import Photo
from .views import AlbumAPIList


class TestAlbumModel(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='test', email='lisa@test.ru', password='test123!@#'
        )
        self.album = Album.objects.create(
            user=self.user,
            album_title='test_album',
            photos_quantity=0,
        )
        return super().setUp()

    def test_create_album(self):
        self.assertEqual(self.album.user, self.user)
        self.assertEqual(self.album.album_title, 'test_album')
        self.assertEqual(self.album.photos_quantity, 0)


class TestPhotoModel(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='test', email='lisa@test.ru', password='test123!@#'
        )
        with transaction.atomic():
            self.album = Album.objects.create(
                user=self.user,
                album_title='test_album',
                photos_quantity=0,
            )

            self.photo = Photo.objects.create(
                album=self.album,
                image_file=SimpleUploadedFile(name='test_image.jpg',
                                         content=open('album/test_media/green-field-with-trees.jpg', 'rb').read(),
                                         content_type='image/jpeg'),
            )
        super().setUp()

    def test_create_photo(self):
        self.assertIn('.jpg', self.photo.image_file.name)
        self.photo.delete()

    # def test_create_thumbnail(self):
    #     self.assertIn('resized.jpg', self.photo.thumbnail.name)
    #     self.photo.delete()

    def test_delete_photo(self):
        self.photo.delete()
        mypath = 'media/image'
        photos = []
        for (dirpath, dirnames, filenames) in walk(mypath):
            photos.extend(filenames)
            break
        self.assertEqual(len(photos), 0)


class TestAPIAlbum(TestCase):

    def setUp(self):
        self.super_user = get_user_model().objects.create_superuser(
            username='admintest', email='admin@test.com', password='Z123xcvbnm'
        )
        self.user = get_user_model().objects.create_user(
            username='test1', email='test1@test.com', password='Z123xcvbnm')

        self.factory = APIRequestFactory()
        self.album = mixer.blend(Album, user=self.user)

    # def test_get_list_quest(self):
    #     view = AlbumAPIList
    #     request = self.factory.get('api/v1/albums/')
    #     # response = view(request)
    #     response = view()
    #     # print(response.render().content.decode('utf-8'))
    #     # self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    #     self.assertEqual(response, status.HTTP_200_OK)

    def test_get_list_user(self):
        view = AlbumAPIList
        request = self.factory.get('api/v1/albums/')
        # force_authenticate(request, user=self.user)
        force_authenticate(request)
        response = view(request)
        # self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response, status.HTTP_200_OK)

    def test_get_detail_quest(self):
        view = AlbumAPIList
        request = self.factory.get(f'api/v1/albums/{self.album.id}')
        # response = view(request, pk=self.album.pk)
        response = view(request)
        # self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response, status.HTTP_200_OK)

    def test_get_detail_user(self):
        view = AlbumAPIList
        request = self.factory.get(f'api/v1/albums/{self.album.id}')
        force_authenticate(request, self.user)
        # response = view(request, pk=self.album.pk)
        response = view(request)
        # self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response, status.HTTP_200_OK)

    # def test_post_quest(self):
    #     view = AlbumAPIList
    #     album_data = {'album_title': 'new_album'}
    #     request = self.factory.post('api/v1/albums/', self.album.album_title, format='json')
    #     # response = view(request)
    #     response = view()
    #     # self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    #     self.assertEqual(response, status.HTTP_200_OK)

    def test_post_user(self):
        view = AlbumAPIList
        album = {'album_title': 'new_album'}
        request = self.factory.post('api/v1/albums/', album, format='json')
        # force_authenticate(request, user=self.user)
        force_authenticate(request)
        response = view(request)
        # self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response, status.HTTP_200_OK)


    def test_delete_quest(self):
        view = AlbumAPIList
        request = self.factory.delete(f'api/v1/albums/{self.album.pk}')
        response = view(request)
        # self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response, status.HTTP_401_UNAUTHORIZED)

    # def test_delete_user(self):
    #     view = AlbumAPIList
    #     request = self.factory.delete(f'api/v1/albums/{self.album.pk}')
    #     # force_authenticate(request, self.user)
    #     force_authenticate(request)
    #     # response = view(request, pk=self.album.pk)
    #     # response = view(request)
    #     # self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    #     self.assertFalse(Album.objects.filter(pk=self.album.id).exists())
