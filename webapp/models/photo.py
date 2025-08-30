from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

IS_PRIVATE_CHOICES = [
    (True, 'Приватное'),
    (False, 'Публичное')
]

def upload_to(instance, filename):
    return f'users/{instance.author}/{filename}'

class Photo(models.Model):
    image = models.ImageField(upload_to=upload_to, verbose_name='Картинка', null=False, blank=False)
    description = models.CharField(max_length=50, verbose_name='Описание', null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    author = models.ForeignKey(get_user_model(), verbose_name='Автор', on_delete=models.RESTRICT, related_name='photos')
    album = models.ForeignKey('webapp.Album', verbose_name='Альбом',
                              on_delete=models.CASCADE, related_name='photos', null=True, blank=True)
    is_private = models.BooleanField(choices=IS_PRIVATE_CHOICES, default=False, verbose_name='Приватность')

    def __str__(self):
        return f"{self.id} | {self.description} | {self.author}"

    class Meta:
        db_table = 'photo'
        verbose_name = 'Фото'
        verbose_name_plural = 'Фотки'

    def get_absolute_url(self):
        return reverse('webapp:photo_detail', kwargs={'pk': self.pk})




