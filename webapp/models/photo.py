from django.contrib.auth import get_user_model
from django.db import models
from webapp.models import Album


def upload_to(instance, filename):
    return f'users/{instance.author}/{filename}'

class Photo(models.Model):
    image = models.ImageField(upload_to=upload_to, verbose_name='Картинка', null=False, blank=False)
    description = models.CharField(max_length=50, verbose_name='Описание', null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    author = models.ForeignKey(get_user_model(), verbose_name='Автор', on_delete=models.RESTRICT, related_name='photos')
    album = models.ForeignKey(Album, verbose_name='Альбом', on_delete=models.CASCADE, related_name='photos')
    is_private = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.id} | {self.description} | {self.author}"

    class Meta:
        db_table = 'photo'
        verbose_name = 'Фото'
        verbose_name_plural = 'Фотки'


