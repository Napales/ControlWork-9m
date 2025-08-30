from django.contrib import admin
from webapp.models import Album, Photo, Favorite

# Register your models here.

admin.site.register(Album)
admin.site.register(Photo)
admin.site.register(Favorite)
