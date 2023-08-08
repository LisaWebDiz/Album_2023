from rest_framework import serializers
from .models import Album, Photo, User, Category





class PhotoSerializer(serializers.ModelSerializer):
    image_file = serializers.SerializerMethodField()
    thumbnail = serializers.SerializerMethodField()
    class Meta:
        model = Photo
        fields = ['image_file', 'album', 'category', 'photo_pub_date', 'thumbnail']

    def get_image_file(self, obj):
        return obj.image_file.url

    def get_thumbnail(self, obj):
        return obj.thumbnail.url


class AlbumSerializer(serializers.ModelSerializer):
    # drf вывести property
    # вставить сериализатор фотографий, чтобы они выводились в постман

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


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['name', 'surname']


class UserAlbumForeignKey(serializers.PrimaryKeyRelatedField):
    """Показывать альбомы принадлежащие юзеру"""

    def get_queryset(self):
        user = self.context['request'].user
        return Album.objects.filter(user=user)



# class CategorySerializer(serializers.ModelSerializer):
#     picture = serializers.SerializerMethodField()
#     thumbnail = serializers.SerializerMethodField()
#     class Meta:
#         model = Category
#         fields = ('id', 'name', 'picture','thumbnail')
#     def get_picture(self, obj):
#         return obj.picture.url
#     def get_thumbnail(self, obj):
#         return obj.thumbnail150x150.url









