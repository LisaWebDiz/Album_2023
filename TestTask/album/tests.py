from django.contrib.auth import get_user_model
from django.test import TestCase

from mixer.backend.django import mixer
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate

from .views import AlbumAPIList
from album.models import Album


class TestAlbumModel(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='test_user', email='test_user@test.ru', password='testuser456^%$'
        )
        self.album = Album.objects.create(
            user=self.user,
            album_title='test_album'
        )
        return super().setUp()

    def test_create_album(self):
        self.assertEqual(self.album.user, self.user)
        self.assertEqual(self.album.album_title, 'test_album')


class TestAPIAlbum(TestCase):

    def setUp(self):
        self.super_user = get_user_model().objects.create_superuser(
            username='testadmin1', email='admin@test.ru', password='*&^678Admin'
        )
        self.user = get_user_model().objects.create_user(
            username='testadmin', email='admin@test.ru', password='*&^678Admin')

        self.factory = APIRequestFactory()
        self.album = mixer.blend(Album, username=self.user)

    def test_get_list_quest(self):
        view = AlbumAPIList.as_view()
        request = self.factory.get('api/v1/albums/')
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


    def test_get_list_user(self):
        view = AlbumAPIList.as_view()
        request = self.factory.get('api/v1/albums/')
        force_authenticate(request, user=self.user)
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_get_detail_user(self):
        view = AlbumAPIList.as_view()
        request = self.factory.get(f'api/v1/albums/{self.album.id}')
        force_authenticate(request, self.user)
        response = view(request, pk=self.album.pk)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_quest(self):
        view = AlbumAPIList.as_view()
        request = self.factory.post('api/v1/albums/', self.album.album_title, format='json')
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_post_user(self):
        view = AlbumAPIList.as_view()
        album = {'album_title': 'test_album'}
        request = self.factory.post('api/v1/albums/', album, format='json')
        force_authenticate(request, user=self.user)
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete_quest(self):
        view = AlbumAPIList.as_view()
        request = self.factory.delete(f'api/v1/albums/{self.album.pk}')
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
