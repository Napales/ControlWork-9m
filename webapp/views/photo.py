from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from webapp.forms import PhotoForm
from webapp.models import Photo


class PhotoListView(ListView):
    model = Photo
    template_name = 'photo/photo_list.html'
    context_object_name = 'photos'
    paginate_by = 6

class PhotoDetailView(LoginRequiredMixin, DetailView):
    template_name = 'photo/photo_detail.html'
    model = Photo
    context_object_name = 'photo'

class PhotoCreateView(LoginRequiredMixin, CreateView):
    template_name = 'photo/photo_create.html'
    model = Photo
    form_class = PhotoForm
    success_url = reverse_lazy('webapp:photo_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)