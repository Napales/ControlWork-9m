from django.urls import path

from webapp.views.photo import PhotoListView

app_name = 'webapp'

urlpatterns = [
    path('', PhotoListView.as_view(), name='photo_list'),
]