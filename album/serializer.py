from rest_framework import serializers
from .models import Album, Photo, Category


class UserAlbumForeignKey(serializers.PrimaryKeyRelatedField):

    def get_queryset(self):
        user = self.context['request'].user
        return Album.objects.filter(user=user)


class PhotoSerializer(serializers.ModelSerializer):
    album = UserAlbumForeignKey()
    thumbnail = serializers.SerializerMethodField()

    class Meta:
        model = Photo
        fields = ['image_file', 'album', 'category', 'photo_pub_date', 'thumbnail']

    def get_image_file(self, obj):
        return obj.image_file.url

    def get_thumbnail(self, obj):
        return obj.thumbnail.url

    def get_queryset(self):
        user = self.context['request'].user
        return Photo.objects.filter(user=user)


class AlbumSerializer(serializers.ModelSerializer):
    album_photos = PhotoSerializer(many=True, read_only=True)

    class Meta:
        model = Album
        fields = ['album_title', 'description', 'album_pub_date', 'photos_quantity', 'album_photos']
        depth = 1


class CategorySerializer(serializers.ModelSerializer):
    photo_category = PhotoSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['cat_title', 'photo_category']


