from django.urls import path

from webapp.views import AlbumDetailView
from webapp.views.album import AlbumCreateView, AlbumDeleteView, AlbumUpdateView
from webapp.views.photo import PhotoListView, PhotoDetailView, PhotoCreateView, PhotoUpdateView, PhotoDeleteView

app_name = 'webapp'

urlpatterns = [
    path('', PhotoListView.as_view(), name='photo_list'),
    path('photo/<int:pk>/', PhotoDetailView.as_view(), name='photo_detail'),
    path('photo/add/', PhotoCreateView.as_view(), name='photo_add'),
    path('photo/<int:pk>/update/', PhotoUpdateView.as_view(), name='photo_update'),
    path('photo/<int:pk>/delete/', PhotoDeleteView.as_view(), name='photo_delete'),

    path('album/<int:pk>/', AlbumDetailView.as_view(), name='album_detail'),
    path('album/add/', AlbumCreateView.as_view(), name='album_add'),
    path('album/<int:pk>/update/', AlbumUpdateView.as_view(), name='album_update'),
    path('album/<int:pk>/delete/', AlbumDeleteView.as_view(), name='album_delete'),
]