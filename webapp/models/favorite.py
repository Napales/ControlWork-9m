from django.contrib.auth import get_user_model
from django.db import models

class Favorite(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='Пользователь', related_name='favorites')
    photo = models.ForeignKey('webapp.Photo', on_delete=models.CASCADE, null=True, blank=True,
                              verbose_name='Фото', related_name='favorites')
    album = models.ForeignKey('webapp.album', on_delete=models.CASCADE, null=True, blank=True,
                              verbose_name='Альбом', related_name='favorites')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')


    def __str__(self):
        return f"{self.id} | {self.user} | {self.photo} | {self.album}"