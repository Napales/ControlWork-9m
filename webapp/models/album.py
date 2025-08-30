from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

IS_PRIVATE_CHOICES = [
    (True, 'Приватное'),
    (False, 'Публичное')
]

class Album(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название', null=False, blank=False)
    description = models.TextField(verbose_name='Описание', null=True, blank=True)
    author = models.ForeignKey(get_user_model(), verbose_name='Автор', on_delete=models.CASCADE,
                               related_name='albums', null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    is_private = models.BooleanField(choices=IS_PRIVATE_CHOICES, default=False, verbose_name='Приватность')

    def __str__(self):
        return f"{self.title}"

    class Meta:
        db_table = 'album'
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'

    def get_absolute_url(self):
        return reverse('webapp:album_detail', kwargs={'pk': self.pk})
