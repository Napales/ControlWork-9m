from django.views.generic import ListView

from webapp.models import Photo


class PhotoListView(ListView):
    model = Photo
    template_name = 'photo/photo_list.html'
    context_object_name = 'photos'
    paginate_by = 10