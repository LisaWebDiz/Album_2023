from django.contrib import admin
from .models import Album, Photo, User, Category


class AlbumAdmin(admin.ModelAdmin):
    list_display = ('id', 'album_title', 'description', 'album_pub_date', 'photos_quantity')
    list_display_links = ('id', 'album_title')
    search_fields = ('album_pub_date', 'user')

    def get_queryset(self, request):
        qs = super(AlbumAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'user', None) is None:
            obj.user = request.user
        obj.save()

admin.site.register(Album, AlbumAdmin)


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'image_file', 'album', 'photo_pub_date', 'thumbnail')
    list_display_links = ('id', 'image_file', 'thumbnail')
    search_fields = ('photo_pub_date', 'album')
    list_filter = ('photo_pub_date', 'album',)

admin.site.register(Photo, PhotoAdmin)


class CategoryAdmin(admin.ModelAdmin):

    list_display = ('id', 'cat_title')
    list_display_links = ('id', 'cat_title')
    search_fields = ('cat_title',)

admin.site.register(Category, CategoryAdmin)
